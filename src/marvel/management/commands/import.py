import threading
import queue
import time
import hashlib
import math
from django.core.management.base import BaseCommand
import requests
from marvel.models import (
    Event,
    Comic,
    Creator,
    Series,
    Character,
    Role,
)


class Command(BaseCommand):
    help = 'Import marvel data from endpoint'
    BASE_URL = 'http://gateway.marvel.com:80/v1/public/'
    MAX_RETRIES = 20
    MAX_THREADS = 8
    q = queue.Queue()
    threads = []

    def worker(self):
        while True:
            item = self.q.get()
            if item is None:
                break
            item[0](item[1])
            self.q.task_done()

    def init_connexion(self):
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=self.MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)
        return session

    def add_arguments(self, parser):
        parser.add_argument('public_key')
        parser.add_argument('private_key')

    def get_resource(self, resource, options):
        timestamp = int(time.time())
        hash_string = str(timestamp) + self.private_key + self.public_key
        hash = hashlib.md5(hash_string.encode('utf-8')).hexdigest()
        url = self.BASE_URL + resource
        parameters = '?ts={ts}&apikey={public_key}&hash={hash}'.format(
            ts=timestamp,
            public_key=self.public_key,
            hash=hash
        )
        for k, v in options.items():
            parameters += '&{key}={value}'.format(key=k, value=v)

        url += parameters
        r = self.session.get(url)
        return r.json()

    def get_full_resource(self, resource):
        first_call = self.get_resource(resource, {'limit': 100})
        total = first_call['data']['total']
        count = first_call['data']['count']
        iterations_needed = int(math.ceil(float(total)/float(count)))
        data = []
        data.extend(first_call['data']['results'])

        for i in range(1, iterations_needed):
            self.q.put([
                lambda x: data.extend(
                    self.get_resource(
                        resource,
                        {'limit': 100, 'offset': 100 * x}
                    )['data']['results']
                ),
                i
            ])

        self.q.join()

        return data

    def update_a_comic(self, resource):
        self.stdout.write(
            'Adding comic {comic_id} to db'.format(
                comic_id=resource['id']
            )
        )
        comic, created = Comic.objects.get_or_create(
            marvel_id=resource['id']
        )
        comic.title = resource['title']
        comic.variant_description = resource['variantDescription']
        comic.description = resource['description']
        comic.page_count = resource['pageCount']
        comic.url = resource['urls'][0]['url']
        comic.date = resource['dates'][0]['date']
        comic.thumbnail = (
            resource['thumbnail']['path']
            + '/portrait_uncanny.'
            + resource['thumbnail']['extension']
        )
        if len(resource['images']) > 0:
            comic.image = (
                resource['images'][0]['path']
                + '/portrait_uncanny.'
                + resource['images'][0]['extension']
            )

        series_id = resource['series']['resourceURI'].rsplit('/', 1)[-1]
        series, created = Series.objects.get_or_create(
            marvel_id=series_id,
            defaults={'title': resource['series']['name']},
        )
        linked_series = comic.series_list.values_list(
            'marvel_id',
            flat=True
        )
        if int(series_id) not in linked_series:
            comic.series_list.add(series_id)

        creators_list = resource['creators']['items']
        for creator_infos in creators_list:
            creator_id = creator_infos['resourceURI'].rsplit('/', 1)[-1]
            creator, created = Creator.objects.get_or_create(
                marvel_id=creator_id,
                defaults={'full_name': creator_infos['name']},
            )
            relation = ''
            if 'role' in creator_infos:
                relation = creator_infos['role']
            role, role_create = Role.objects.get_or_create(
                creator=creator,
                comic=comic,
                defaults={'role': relation}
            )

        characters_list = resource['characters']['items']
        for character_infos in characters_list:
            character_id = character_infos['resourceURI'].rsplit('/', 1)[-1]
            character, created = Character.objects.get_or_create(
                marvel_id=character_id,
                defaults={'name': character_infos['name']},
            )
            linked_characters = comic.characters.values_list(
                'marvel_id',
                flat=True
            )
            if int(character_id) not in linked_characters:
                comic.characters.add(character_id)

        events_list = resource['events']['items']
        for event_infos in events_list:
            event_id = event_infos['resourceURI'].rsplit('/', 1)[-1]
            event, created = Event.objects.get_or_create(
                marvel_id=event_id,
                default={'title': event_infos['title']},
            )
            linked_events = comic.events.values_list(
                'marvel_id',
                flat=True
            )
            if int(event_id) not in linked_events:
                comic.events.add(event_id)

        comic.save()

    def update_an_event(self, resource):
        self.stdout.write(
            'Adding event {event_id} to db'.format(
                event_id=resource['id']
            )
        )
        event, created = Event.objects.get_or_create(
            marvel_id=resource['id']
        )
        event.title = resource['title']
        event.description = resource['description']
        event.url = resource['urls'][0]['url']
        event.start = resource['start']
        event.end = resource['end']
        event.thumbnail = (
            resource['thumbnail']['path']
            + '/portrait_uncanny.'
            + resource['thumbnail']['extension']
        )

        series_list = resource['series']['items']
        for series_infos in series_list:
            series_id = series_infos['resourceURI'].rsplit('/', 1)[-1]
            series, created = Series.objects.get_or_create(
                marvel_id=series_id,
                defaults={'title': series_infos['name']},
            )
            linked_series = event.series_list.values_list(
                'marvel_id',
                flat=True
            )
            if int(series_id) not in linked_series:
                event.series_list.add(series_id)

        creators_list = resource['creators']['items']
        for creator_infos in creators_list:
            creator_id = creator_infos['resourceURI'].rsplit('/', 1)[-1]
            creator, created = Creator.objects.get_or_create(
                marvel_id=creator_id,
                defaults={'full_name': creator_infos['name']},
            )
            linked_creators = event.creators.values_list(
                'marvel_id',
                flat=True
            )
            if int(creator_id) not in linked_creators:
                event.creators.add(creator_id)

        characters_list = resource['characters']['items']
        for character_infos in characters_list:
            character_id = character_infos['resourceURI'].rsplit('/', 1)[-1]
            character, created = Character.objects.get_or_create(
                marvel_id=character_id,
                defaults={'name': character_infos['name']},
            )
            linked_characters = event.characters.values_list(
                'marvel_id',
                flat=True
            )
            if int(character_id) not in linked_characters:
                event.characters.add(character_id)

        comics_list = resource['comics']['items']
        for comic_infos in comics_list:
            comic_id = comic_infos['resourceURI'].rsplit('/', 1)[-1]
            comic, created = Comic.objects.get_or_create(
                marvel_id=comic_id,
                defaults={'title': comic_infos['name']},
            )
            linked_comics = event.comics.values_list(
                'marvel_id',
                flat=True
            )
            if int(comic_id) not in linked_comics:
                event.comics.add(comic_id)

        event.save()

    def update_a_series(self, resource):
        self.stdout.write(
            'Adding series {series_id} to db'.format(
                series_id=resource['id']
            )
        )
        series, created = Series.objects.get_or_create(
            marvel_id=resource['id']
        )
        series.title = resource['title']
        series.description = resource['description']
        series.url = resource['urls'][0]['url']
        series.start_year = resource['startYear']
        series.end_year = resource['endYear']
        series.thumbnail = (
            resource['thumbnail']['path']
            + '/portrait_uncanny.'
            + resource['thumbnail']['extension']
        )

        creators_list = resource['creators']['items']
        for creator_infos in creators_list:
            creator_id = creator_infos['resourceURI'].rsplit('/', 1)[-1]
            creator, created = Creator.objects.get_or_create(
                marvel_id=creator_id,
                defaults={'full_name': creator_infos['name']},
            )
            linked_creators = series.creators.values_list(
                'marvel_id',
                flat=True
            )
            if int(creator_id) not in linked_creators:
                series.creators.add(creator_id)

        characters_list = resource['characters']['items']
        for character_infos in characters_list:
            character_id = character_infos['resourceURI'].rsplit('/', 1)[-1]
            character, created = Character.objects.get_or_create(
                marvel_id=character_id,
                defaults={'name': character_infos['name']},
            )
            linked_characters = series.characters.values_list(
                'marvel_id',
                flat=True
            )
            if int(character_id) not in linked_characters:
                series.characters.add(character_id)

        events_list = resource['events']['items']
        for event_infos in events_list:
            event_id = event_infos['resourceURI'].rsplit('/', 1)[-1]
            event, created = Event.objects.get_or_create(
                marvel_id=event_id,
                defaults={'name': event_infos['name']},
            )
            linked_events = series.events.values_list(
                'marvel_id',
                flat=True
            )
            if int(event_id) not in linked_events:
                series.events.add(event_id)

        comics_list = resource['comics']['items']
        for comic_infos in comics_list:
            comic_id = comic_infos['resourceURI'].rsplit('/', 1)[-1]
            comic, created = Comic.objects.get_or_create(
                marvel_id=comic_id,
                defaults={'title': comic_infos['name']},
            )
            linked_comics = series.comics.values_list(
                'marvel_id',
                flat=True
            )
            if int(comic_id) not in linked_comics:
                series.comics.add(comic_id)

        series.save()

    def update_a_creator(self, resource):
        self.stdout.write(
            'Adding creator {creator_id} to db'.format(
                creator_id=resource['id']
            )
        )
        creator, created = Creator.objects.get_or_create(
            marvel_id=resource['id']
        )
        creator.first_name = resource['firstName']
        creator.last_name = resource['lastName']
        creator.suffix = resource['suffix']
        creator.full_name = resource['fullName']
        creator.url = resource['urls'][0]['url']
        creator.thumbnail = (
            resource['thumbnail']['path']
            + '/portrait_uncanny.'
            + resource['thumbnail']['extension']
        )

        series_list = resource['series']['items']
        for series_infos in series_list:
            series_id = series_infos['resourceURI'].rsplit('/', 1)[-1]
            series, created = Series.objects.get_or_create(
                marvel_id=series_id,
                defaults={'title': series_infos['name']},
            )
            linked_series = creator.series_list.values_list(
                'marvel_id',
                flat=True
            )
            if int(series_id) not in linked_series:
                creator.series_list.add(series_id)

        comics_list = resource['comics']['items']
        for comic_infos in comics_list:
            comic_id = comic_infos['resourceURI'].rsplit('/', 1)[-1]
            comic, created = Comic.objects.get_or_create(
                marvel_id=comic_id,
                defaults={'title': comic_infos['name']},
            )
            relation = ''
            if 'role' in comic_infos:
                relation = comic_infos['role']
            role, role_create = Role.objects.get_or_create(
                creator=creator,
                comic=comic,
                defaults={'role': relation}
            )

        events_list = resource['events']['items']
        for event_infos in events_list:
            event_id = event_infos['resourceURI'].rsplit('/', 1)[-1]
            event_title = ''
            if 'title' in event_infos:
                event_title = event_infos['title']
            event, created = Event.objects.get_or_create(
                marvel_id=event_id,
                defaults={'title': event_title},
            )
            linked_events = creator.events.values_list(
                'marvel_id',
                flat=True
            )
            if int(event_id) not in linked_events:
                creator.events.add(event_id)

        creator.save()

    def update_a_character(self, resource):
        self.stdout.write(
            'Adding character {character_id} to db'.format(
                character_id=resource['id']
            )
        )
        character, created = Character.objects.get_or_create(
            marvel_id=resource['id']
        )
        character.name = resource['name']
        character.description = resource['description']
        character.url = resource['urls'][0]['url']
        character.thumbnail = (
            resource['thumbnail']['path']
            + '/portrait_uncanny.'
            + resource['thumbnail']['extension']
        )

        series_list = resource['series']['items']
        for series_infos in series_list:
            series_id = series_infos['resourceURI'].rsplit('/', 1)[-1]
            series, created = Series.objects.get_or_create(
                marvel_id=series_id,
                defaults={'title': series_infos['name']},
            )
            linked_series = character.series_list.values_list(
                'marvel_id',
                flat=True
            )
            if int(series_id) not in linked_series:
                character.series_list.add(series_id)

        events_list = resource['events']['items']
        for event_infos in events_list:
            event_id = event_infos['resourceURI'].rsplit('/', 1)[-1]
            event, created = Event.objects.get_or_create(
                marvel_id=event_id,
                defaults={'title': event_infos['name']},
            )
            linked_events = character.events.values_list(
                'marvel_id',
                flat=True
            )
            if int(event_id) not in linked_events:
                character.events.add(event_id)

        comics_list = resource['comics']['items']
        for comic_infos in comics_list:
            comic_id = comic_infos['resourceURI'].rsplit('/', 1)[-1]
            comic, created = Comic.objects.get_or_create(
                marvel_id=comic_id,
                defaults={'title': comic_infos['name']},
            )
            linked_comics = character.comics.values_list(
                'marvel_id',
                flat=True
            )
            if int(comic_id) not in linked_comics:
                character.comics.add(comic_id)

        character.save()

    def update_resource_by_type(self, name, endpoint, method):
        self.stdout.write('---------------------')
        self.stdout.write('Start {name} import'.format(name=name))
        self.stdout.write('Loading data from Marvel api')
        new_resources = self.get_full_resource(endpoint)
        self.stdout.write('Data loaded')
        self.stdout.write('--')

        for resource in new_resources:
            self.q.put([
                method,
                resource
            ])

        self.q.join()
        self.stdout.write('Finished {name} import'.format(name=name))

    def handle(self, *args, **options):
        self.private_key = options['private_key']
        self.public_key = options['public_key']
        self.session = self.init_connexion()

        for i in range(self.MAX_THREADS):
            t = threading.Thread(target=self.worker)
            t.start()
            self.threads.append(t)

        resources = [
            {'name': 'Comics', 'endpoint': 'comics', 'method': self.update_a_comic},
            {'name': 'Events', 'endpoint': 'events', 'method': self.update_an_event},
            {'name': 'Creators', 'endpoint': 'creators', 'method': self.update_a_creator},
            {'name': 'Series', 'endpoint': 'series', 'method': self.update_a_series},
            {'name': 'Characters', 'endpoint': 'characters', 'method': self.update_a_character},
        ]
        for resource in resources:
            self.update_resource_by_type(
                resource['name'],
                resource['endpoint'],
                resource['method']
            )

        # stop workers
        for j in range(self.MAX_THREADS):
            self.q.put(None)
        for t in self.threads:
            t.join()

        self.stdout.write(
            self.style.SUCCESS('Successfully imported marvel data')
        )
