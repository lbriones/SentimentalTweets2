# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertw', models.TextField(verbose_name='UserTw', blank=True)),
                ('text', models.TextField(null=True, verbose_name='Tweet', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('screen_name', models.CharField(max_length=50, verbose_name='Screen name')),
                ('screen_id', models.CharField(unique=True, max_length=100, verbose_name='Id', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('timeline', models.TextField(null=True, verbose_name='Timeline', blank=True)),
            ],
        ),
    ]
