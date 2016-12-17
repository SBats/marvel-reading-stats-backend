import requests
import math
import time
import hashlib
from multiprocessing import pool
from django.core.management.base import BaseCommand
from marvel.models import (
    Event,
    Comic,
    Creator,
    Series,
    Character,
    Role,
    MarvelImage
)

BASE_URL = 'http://gateway.marvel.com:80/v1/public/'
MAX_RETRIES = 20
TIMEOUT = 1200
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=100,
    max_retries=MAX_RETRIES
)
session.mount('https://', adapter)
session.mount('http://', adapter)


def get_resource(url):
    count = MAX_RETRIES
    status = 0
    result = None
    while (status < 200 or status >= 300) and count > 0:
        r = session.get(url, timeout=TIMEOUT)
        status = r.status_code
        result = r.json()
        count -= 1

    if result is not None:
        return result
    else:
        raise Exception(
            "Exceeded max retry for url: {url}".format(url=url)
        )


def get_resource_data(url):
    print(url)
    r = get_resource(url)
    return r.get('data').get('results')


def update_a_comic(resource):
    print(
        'Adding comic {comic_id} to db'.format(
            comic_id=resource.get('id')
        )
    )
    comic, created = Comic.objects.get_or_create(
        marvel_id=resource.get('id')
    )
    comic.title = resource.get('title')
    comic.variant_description = resource.get('variantDescription')
    comic.description = resource.get('description')
    comic.page_count = resource.get('pageCount')
    comic.url = resource.get('urls')[0].get('url') if resource.get('urls')[0] else ''
    comic.date = resource.get('dates')[0].get('date') if resource.get('dates')[0] else None
    new_image, created = MarvelImage.objects.get_or_create(
        path=resource.get('thumbnail').get('path'),
        extension=resource.get('thumbnail').get('extension')
    )
    comic.image = new_image

    series_id = resource.get('series').get('resourceURI').rsplit('/', 1)[-1]
    series, created = Series.objects.get_or_create(
        marvel_id=series_id,
        defaults={'title': resource.get('series').get('name')},
    )
    linked_series = comic.series_list.values_list(
        'marvel_id',
        flat=True
    )
    if int(series_id) not in linked_series:
        comic.series_list.add(series_id)

    creators_list = resource.get('creators').get('items')
    for creator_infos in creators_list:
        creator_id = creator_infos.get('resourceURI').rsplit('/', 1)[-1]
        creator, created = Creator.objects.get_or_create(
            marvel_id=creator_id,
            defaults={'full_name': creator_infos.get('name')},
        )
        relation = ''
        if 'role' in creator_infos:
            relation = creator_infos.get('role')
        role, role_create = Role.objects.get_or_create(
            creator=creator,
            comic=comic,
            defaults={'role': relation}
        )

    characters_list = resource.get('characters').get('items')
    for character_infos in characters_list:
        character_id = character_infos.get('resourceURI').rsplit('/', 1)[-1]
        character, created = Character.objects.get_or_create(
            marvel_id=character_id,
            defaults={'name': character_infos.get('name')},
        )
        linked_characters = comic.characters.values_list(
            'marvel_id',
            flat=True
        )
        if int(character_id) not in linked_characters:
            comic.characters.add(character_id)

    events_list = resource.get('events').get('items')
    for event_infos in events_list:
        event_id = event_infos.get('resourceURI').rsplit('/', 1)[-1]
        event, created = Event.objects.get_or_create(
            marvel_id=event_id,
            defaults={'title': event_infos.get('title')},
        )
        linked_events = comic.events.values_list(
            'marvel_id',
            flat=True
        )
        if int(event_id) not in linked_events:
            comic.events.add(event_id)

    comic.save()


def update_an_event(resource):
    print(
        'Adding event {event_id} to db'.format(
            event_id=resource.get('id')
        )
    )
    event, created = Event.objects.get_or_create(
        marvel_id=resource.get('id')
    )
    event.title = resource.get('title')
    event.description = resource.get('description')
    event.url = resource.get('urls')[0].get('url') if resource.get('urls')[0] else ''
    event.start = resource.get('start')
    event.end = resource.get('end')
    new_image, created = MarvelImage.objects.get_or_create(
        path=resource.get('thumbnail').get('path'),
        extension=resource.get('thumbnail').get('extension')
    )
    event.image = new_image

    series_list = resource.get('series').get('items')
    for series_infos in series_list:
        series_id = series_infos.get('resourceURI').rsplit('/', 1)[-1]
        series, created = Series.objects.get_or_create(
            marvel_id=series_id,
            defaults={'title': series_infos.get('name')},
        )
        linked_series = event.series_list.values_list(
            'marvel_id',
            flat=True
        )
        if int(series_id) not in linked_series:
            event.series_list.add(series_id)

    creators_list = resource.get('creators').get('items')
    for creator_infos in creators_list:
        creator_id = creator_infos.get('resourceURI').rsplit('/', 1)[-1]
        creator, created = Creator.objects.get_or_create(
            marvel_id=creator_id,
            defaults={'full_name': creator_infos.get('name')},
        )
        linked_creators = event.creators.values_list(
            'marvel_id',
            flat=True
        )
        if int(creator_id) not in linked_creators:
            event.creators.add(creator_id)

    characters_list = resource.get('characters').get('items')
    for character_infos in characters_list:
        character_id = character_infos.get('resourceURI').rsplit('/', 1)[-1]
        character, created = Character.objects.get_or_create(
            marvel_id=character_id,
            defaults={'name': character_infos.get('name')},
        )
        linked_characters = event.characters.values_list(
            'marvel_id',
            flat=True
        )
        if int(character_id) not in linked_characters:
            event.characters.add(character_id)

    comics_list = resource.get('comics').get('items')
    for comic_infos in comics_list:
        comic_id = comic_infos.get('resourceURI').rsplit('/', 1)[-1]
        comic, created = Comic.objects.get_or_create(
            marvel_id=comic_id,
            defaults={'title': comic_infos.get('name')},
        )
        linked_comics = event.comics.values_list(
            'marvel_id',
            flat=True
        )
        if int(comic_id) not in linked_comics:
            event.comics.add(comic_id)

    event.save()


def update_a_series(resource):
    print(
        'Adding series {series_id} to db'.format(
            series_id=resource.get('id')
        )
    )
    series, created = Series.objects.get_or_create(
        marvel_id=resource.get('id')
    )
    series.title = resource.get('title')
    series.description = resource.get('description')
    series.url = resource.get('urls')[0].get('url') if resource.get('urls')[0] else ''
    series.start_year = resource.get('startYear')
    series.end_year = resource.get('endYear')
    new_image, created = MarvelImage.objects.get_or_create(
        path=resource.get('thumbnail').get('path'),
        extension=resource.get('thumbnail').get('extension')
    )
    series.image = new_image

    creators_list = resource.get('creators').get('items')
    for creator_infos in creators_list:
        creator_id = creator_infos.get('resourceURI').rsplit('/', 1)[-1]
        creator, created = Creator.objects.get_or_create(
            marvel_id=creator_id,
            defaults={'full_name': creator_infos.get('name')},
        )
        linked_creators = series.creators.values_list(
            'marvel_id',
            flat=True
        )
        if int(creator_id) not in linked_creators:
            series.creators.add(creator_id)

    characters_list = resource.get('characters').get('items')
    for character_infos in characters_list:
        character_id = character_infos.get('resourceURI').rsplit('/', 1)[-1]
        character, created = Character.objects.get_or_create(
            marvel_id=character_id,
            defaults={'name': character_infos.get('name')},
        )
        linked_characters = series.characters.values_list(
            'marvel_id',
            flat=True
        )
        if int(character_id) not in linked_characters:
            series.characters.add(character_id)

    events_list = resource.get('events').get('items')
    for event_infos in events_list:
        event_id = event_infos.get('resourceURI').rsplit('/', 1)[-1]
        event, created = Event.objects.get_or_create(
            marvel_id=event_id,
            defaults={'name': event_infos.get('name')},
        )
        linked_events = series.events.values_list(
            'marvel_id',
            flat=True
        )
        if int(event_id) not in linked_events:
            series.events.add(event_id)

    comics_list = resource.get('comics').get('items')
    for comic_infos in comics_list:
        comic_id = comic_infos.get('resourceURI').rsplit('/', 1)[-1]
        comic, created = Comic.objects.get_or_create(
            marvel_id=comic_id,
            defaults={'title': comic_infos.get('name')},
        )
        linked_comics = series.comics.values_list(
            'marvel_id',
            flat=True
        )
        if int(comic_id) not in linked_comics:
            series.comics.add(comic_id)

    series.save()


def update_a_creator(resource):
    print(
        'Adding creator {creator_id} to db'.format(
            creator_id=resource.get('id')
        )
    )
    creator, created = Creator.objects.get_or_create(
        marvel_id=resource.get('id')
    )
    creator.first_name = resource.get('firstName')
    creator.last_name = resource.get('lastName')
    creator.suffix = resource.get('suffix')
    creator.full_name = resource.get('fullName')
    creator.url = resource.get('urls')[0].get('url')
    new_image, created = MarvelImage.objects.get_or_create(
        path=resource.get('thumbnail').get('path'),
        extension=resource.get('thumbnail').get('extension')
    )
    creator.image = new_image

    series_list = resource.get('series').get('items')
    for series_infos in series_list:
        series_id = series_infos.get('resourceURI').rsplit('/', 1)[-1]
        series, created = Series.objects.get_or_create(
            marvel_id=series_id,
            defaults={'title': series_infos.get('name')},
        )
        linked_series = creator.series_list.values_list(
            'marvel_id',
            flat=True
        )
        if int(series_id) not in linked_series:
            creator.series_list.add(series_id)

    comics_list = resource.get('comics').get('items')
    for comic_infos in comics_list:
        comic_id = comic_infos.get('resourceURI').rsplit('/', 1)[-1]
        comic, created = Comic.objects.get_or_create(
            marvel_id=comic_id,
            defaults={'title': comic_infos.get('name')},
        )
        relation = ''
        if 'role' in comic_infos:
            relation = comic_infos.get('role')
        role, role_create = Role.objects.get_or_create(
            creator=creator,
            comic=comic,
            defaults={'role': relation}
        )

    events_list = resource.get('events').get('items')
    for event_infos in events_list:
        event_id = event_infos.get('resourceURI').rsplit('/', 1)[-1]
        event_title = ''
        if 'title' in event_infos:
            event_title = event_infos.get('title')
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


def update_a_character(resource):
    print(
        'Adding character {character_id} to db'.format(
            character_id=resource.get('id')
        )
    )
    character, created = Character.objects.get_or_create(
        marvel_id=resource.get('id')
    )
    character.name = resource.get('name')
    character.description = resource.get('description')
    character.url = resource.get('urls')[0].get('url') if resource.get('urls')[0] else ''
    new_image, created = MarvelImage.objects.get_or_create(
        path=resource.get('thumbnail').get('path'),
        extension=resource.get('thumbnail').get('extension')
    )
    character.image = new_image

    series_list = resource.get('series').get('items')
    for series_infos in series_list:
        series_id = series_infos.get('resourceURI').rsplit('/', 1)[-1]
        series, created = Series.objects.get_or_create(
            marvel_id=series_id,
            defaults={'title': series_infos.get('name')},
        )
        linked_series = character.series_list.values_list(
            'marvel_id',
            flat=True
        )
        if int(series_id) not in linked_series:
            character.series_list.add(series_id)

    events_list = resource.get('events').get('items')
    for event_infos in events_list:
        event_id = event_infos.get('resourceURI').rsplit('/', 1)[-1]
        event, created = Event.objects.get_or_create(
            marvel_id=event_id,
            defaults={'title': event_infos.get('name')},
        )
        linked_events = character.events.values_list(
            'marvel_id',
            flat=True
        )
        if int(event_id) not in linked_events:
            character.events.add(event_id)

    comics_list = resource.get('comics').get('items')
    for comic_infos in comics_list:
        comic_id = comic_infos.get('resourceURI').rsplit('/', 1)[-1]
        comic, created = Comic.objects.get_or_create(
            marvel_id=comic_id,
            defaults={'title': comic_infos.get('name')},
        )
        linked_comics = character.comics.values_list(
            'marvel_id',
            flat=True
        )
        if int(comic_id) not in linked_comics:
            character.comics.add(comic_id)

    character.save()


class Command(BaseCommand):
    help = 'Import marvel data from endpoint'

    def get_data_url(self, resource, options):
        timestamp = int(time.time())
        hash_string = str(timestamp) + self.private_key + self.public_key
        hash = hashlib.md5(hash_string.encode('utf-8')).hexdigest()
        url = BASE_URL + resource
        parameters = '?ts={ts}&apikey={public_key}&hash={hash}'.format(
            ts=timestamp,
            public_key=self.public_key,
            hash=hash
        )
        for k, v in options.items():
            parameters += '&{key}={value}'.format(key=k, value=v)

        return url + parameters

    def get_resource_urls(self, resource):
        urls = []
        first_url = self.get_data_url(resource, {'limit': 100})
        first_resource = get_resource(first_url)
        total = first_resource.get('data').get('total')
        count = first_resource.get('data').get('count')
        iterations_needed = int(math.ceil(float(total)/float(count)))

        for i in range(0, iterations_needed):
            urls.append(self.get_data_url(
                resource,
                {'limit': 100, 'offset': 100 * i}
            ))

        return urls

    def add_arguments(self, parser):
        parser.add_argument('public_key')
        parser.add_argument('private_key')

    def handle(self, *args, **options):
        self.private_key = options.get('private_key')
        self.public_key = options.get('public_key')
        resources = [
            # {
            #     'name': 'Comics',
            #     'endpoint': 'comics',
            #     'method': update_a_comic
            # },
            # {
            #     'name': 'Events',
            #     'endpoint': 'events',
            #     'method': update_an_event
            # },
            {
                'name': 'Creators',
                'endpoint': 'creators',
                'method': update_a_creator
            },
            {
                'name': 'Series',
                'endpoint': 'series',
                'method': update_a_series
            },
            {
                'name': 'Characters',
                'endpoint': 'characters',
                'method': update_a_character
            },
        ]

        for resource in resources:
            p1 = pool.Pool(processes=100)
            urls = self.get_resource_urls(resource.get('endpoint'))
            data = p1.map_async(get_resource_data, urls).get()
            p1.close()
            p1.join()
            p2 = pool.Pool(processes=50)
            p2.map_async(
                resource.get('method'),
                [item for sublist in data for item in sublist]
            )
            p2.close()
            p2.join()

