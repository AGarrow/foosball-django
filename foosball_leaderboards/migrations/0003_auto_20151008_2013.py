# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foosball_leaderboards', '0002_auto_20151008_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='goals_against',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='win_percentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
