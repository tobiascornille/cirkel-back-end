# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location_lat',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location_lon',
            field=models.FloatField(blank=True),
        ),
    ]
