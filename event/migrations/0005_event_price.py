# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-11-30 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20181130_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
