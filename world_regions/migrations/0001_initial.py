# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management import call_command
from django.db import models, migrations
import django_countries.fields


def load_data_in_fixtures(apps, schema_editor):
    call_command('loaddata', 'initial_data', app_label='world_regions')


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='RegionCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', django_countries.fields.CountryField(unique=True, max_length=2)),
                ('region', models.ForeignKey(related_name='countries', to='world_regions.Region')),
            ],
        ),
        migrations.RunPython(load_data_in_fixtures),
    ]
