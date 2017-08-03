# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts
from ...models import CohortsYear

from ...schemas.cohorts.schema import SCHEMA


class Command(BaseCommand):
    help = 'Loads a school year worth of cohorts data.'

    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)
        # parser.add_argument('--bulk', action='store_true')

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

        # self.use_bulk = options['bulk']

        # get cohorts folder
        cohorts_folder = os.path.join(settings.DATA_FOLDER, 'cohorts')

        # make sure year passed in actually has folder
        self.year_folder = os.path.join(cohorts_folder, options['year'])

        if not os.path.isdir(self.year_folder):
            raise CommandError(
                '`{}` was not found in your cohorts data directory'.format(
                    self.year_folder))

        # if it is there, we get or create our CohortsYear model
        year, _ = CohortsYear.objects.get_or_create(
            name=options['year'])

        self.year = year

        self.load_data()

    def get_state_model_instance(self):
        # name is a parameter set in the mapping.py file that
        # I set this manually as state or region
        return State.objects.get(name='TX')

    def get_region_model_instance(self, identifier, instance):
        # name is a parameter set in the mapping.py file that
        # I set this manually as state or region
        return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    def load_data(self):
        # # Finds the file based on what the schema dict is called
        file_names = ['{}.csv'.format(
            schema) for (schema, _) in SCHEMA.items()]

        data = []
        for file_name in file_names:
            data_file = os.path.join(self.year_folder, file_name)

            with open(data_file) as f:
                reader = csv.DictReader(f)
                data.append([i for i in reader])

            id_match = 'Region Code'

            for row in sum(data, []):
                if row[id_match] is '' or None:

                    payload = {
                        'year': self.year,
                        'defaults': {}
                    }
                    model = self.get_state_model_instance()
                    payload['state'] = model

                    for schema_type, schema in SCHEMA.items():
                        payload['defaults'].update(self.prepare_row(
                            schema, row))

                    payload['ethnicity'] = payload['defaults']['ethnicity']
                    payload['gender'] = payload['defaults']['gender']
                    payload['economic_status'] = payload['defaults']['economic_status']

                    StateCohorts.objects.update_or_create(**payload)

                    self.stdout.write(model.name)
                else:
                    if row[id_match] in ['1', '2', '3', '4', '5', '6',
                                         '7', '8', '9']:
                        identifier = '0' + row[id_match]
                    else:
                        identifier = row[id_match]

                    payload = {
                        'year': self.year,
                        'defaults': {}
                    }
                    model = self.get_region_model_instance(identifier, Region)
                    payload['region'] = model

                    self.stdout.write(model.name)

                    for schema_type, schema in SCHEMA.items():
                        payload['defaults'].update(self.prepare_row(
                            schema, row))

                    payload['ethnicity'] = payload['defaults']['ethnicity']
                    payload['gender'] = payload['defaults']['gender']
                    payload['economic_status'] = payload['defaults']['economic_status']
                    RegionCohorts.objects.update_or_create(**payload)

    def prepare_row(self, schema, row):
        payload = {}

        for field, code in schema.items():
            datum = row[code]
            payload[field] = datum

        return payload
