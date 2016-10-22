import time
import hashlib
import math
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Import marvel data from endpoint'
    base_url = 'http://gateway.marvel.com:80/v1/public/'
    endpoints = [
        'events'
    ]

    def add_arguments(self, parser):
        parser.add_argument('public_key')
        parser.add_argument('private_key')

    def getResource(self, resource, options):
        timestamp = int(time.time())
        hash_string = str(timestamp) + self.private_key + self.public_key
        hash = hashlib.md5(hash_string.encode('utf-8')).hexdigest()
        url = self.base_url + resource
        parameters = '?ts={ts}&apikey={public_key}&hash={hash}'.format(
            ts=timestamp,
            public_key=self.public_key,
            hash=hash
        )
        for k, v in options.items():
            parameters += '&{key}={value}'.format(key=k, value=v)

        url += parameters
        r = requests.get(url)
        return r.json()

    def getFullResource(self, resource):
        first_call = self.getResource(resource, {'limit': 20})
        total = first_call['data']['total']
        count = first_call['data']['count']
        iterations_needed = int(math.ceil(float(total)/float(count)))
        data = []
        data.extend(first_call['data']['results'])

        for i in range(1, iterations_needed):
            query = self.getResource(
                resource,
                {'limit': 100, 'offset': 100 * i}
            )
            data.extend(query['data']['results'])

        return data

    def handle(self, *args, **options):
        self.private_key = options['private_key']
        self.public_key = options['public_key']

        print(self.getFullResource('events'))

        self.stdout.write(
            self.style.SUCCESS('Successfully imported marvel data')
        )
