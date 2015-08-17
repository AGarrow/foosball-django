# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='black',
            field=models.ForeignKey(related_name='black_player', verbose_name=b'Black Player', to='foosball_leaderboards.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='silver',
            field=models.ForeignKey(related_name='silver_player', verbose_name=b'Silver Player', to='foosball_leaderboards.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(related_name='winner', verbose_name=b'the winner of the game', to='foosball_leaderboards.Player'),
        ),
    ]
