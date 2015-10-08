# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foosball_leaderboards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='black_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 4, 13, 38, 828669, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.ForeignKey(related_name='loser', verbose_name=b'loser of the game', to='foosball_leaderboards.Player', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='silver_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 4, 13, 46, 380877, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
