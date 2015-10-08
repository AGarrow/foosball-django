# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foosball_leaderboards', '0003_auto_20151008_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='goal_ratio',
            field=models.FloatField(default=0.0),
        ),
    ]
