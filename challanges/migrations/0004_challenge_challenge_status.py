# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-14 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challanges', '0003_auto_20161013_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='challenge_status',
            field=models.IntegerField(choices=[(1, b'In progress'), (2, b'Complete')], default=1),
        ),
    ]
