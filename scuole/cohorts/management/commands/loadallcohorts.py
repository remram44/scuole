# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from scuole.counties.models import County, CountyCohorts
from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts
from ...models import CohortsYear

from slugify import slugify


class Command(BaseCommand):
    help = 'Loads a school year worth of cohorts data.'

    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

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

        self.load_counties()
        self.load_regions_state()

    def get_state_model_instance(self):
        return State.objects.get(name='TX')

    def get_region_model_instance(self, identifier, instance):
        return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    def get_county_model_instance(self, identifier, instance):
        return instance.objects.get(fips=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Count not find {}'.format(identifier))
            return None

        return model

    def load_regions_state(self):
        data = []

        data_file = os.path.join(self.year_folder, 'regionState.csv')

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

                payload['defaults'].update(self.prepare_row(row))

                payload['ethnicity'] = payload['defaults']['ethnicity']
                payload['gender'] = payload['defaults']['gender']
                payload['economic_status'] = payload['defaults']['economic_status']

                print(payload)

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

                payload['defaults'].update(self.prepare_row(row))

                payload['ethnicity'] = payload['defaults']['ethnicity']
                payload['gender'] = payload['defaults']['gender']
                payload['economic_status'] = payload['defaults']['economic_status']
                RegionCohorts.objects.update_or_create(**payload)

    def load_counties(self):
        counties_fips_id_file = os.path.join(
            self.year_folder, 'county-fips-id-map.csv')

        cohorts_files = [
            os.path.join(self.year_folder, 'countyEcon.csv'),
            os.path.join(self.year_folder, 'countyGender.csv'),
            os.path.join(self.year_folder, 'countyEthnicity.csv')]

        counties = []
        with open(counties_fips_id_file) as f:
            reader = csv.DictReader(f)
            counties.append([i for i in reader])

        data = []
        for file_name in cohorts_files:
            with open(file_name) as f:
                reader = csv.DictReader(f)
                data.append([i for i in reader])

        for row in sum(data, []):
            # This is bad and I know it.
            # Loops through the counties in the FIPS/THECB id map sheet
            # and matches it to the FIPS code stored in the County model
            master_name = slugify(row['County Name'])
            for i in sum(counties, []):
                map_name = slugify(i['THECB County Name'])
                if master_name == map_name:
                    identifier = i['FIPS'].zfill(3)

            payload = {
                'year': self.year,
                'defaults': {}
            }

            model = self.get_county_model_instance(identifier, County)
            payload['county'] = model

            self.stdout.write(model.name)

            payload['defaults'].update(self.prepare_row(row))

            payload['economic_status'] = payload['defaults'].get('economic_status', '')
            payload['gender'] = payload['defaults'].get('gender', '')
            payload['ethnicity'] = payload['defaults'].get('ethnicity', '')

            CountyCohorts.objects.sum_update_or_create(**payload)

    def prepare_row(self, row):
        fields = [
            'enrolled_8th',
            'enrolled_9th',
            'enrolled_9th_percent',
            'enrolled_10th',
            'enrolled_10th_percent',
            'lessthan_10th_enrolled',
            'lessthan_10th_enrolled_percent',
            'graduated',
            'graduated_percent',
            'enrolled_4yr',
            'enrolled_4yr_percent',
            'enrolled_2yr',
            'enrolled_2yr_percent',
            'enrolled_out_of_state',
            'enrolled_out_of_state_percent',
            'total_enrolled',
            'total_enrolled_percent',
            'enrolled_wo_record',
            'enrolled_wo_record_percent',
            'total_degrees',
            'total_degrees_percent',
            'ethnicity',
            'gender',
            'economic_status'
        ]

        problem_children = ['', '-', '.']
        pivots = ['ethnicity', 'gender', 'economic_status']
        payload = {}

        for field in row:
            if field in fields:
                datum = row[field]
                if datum.strip() in problem_children:
                    if field in pivots:
                        datum = ''
                    else:
                        datum = None
                else:
                    datum = row[field]

                payload[field] = datum
            # if field in fields:
            #     datum = row[field]
            #     payload[field] = datum

        return payload
