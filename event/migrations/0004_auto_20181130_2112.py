# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-11-30 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20181130_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='AgeRestriction',
            field=models.IntegerField(),
        ),
    ]
