# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swear',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('bjorn', models.IntegerField()),
                ('alex', models.IntegerField()),
                ('wang', models.IntegerField()),
                ('patrick', models.IntegerField()),
                ('dario', models.IntegerField()),
                ('davide', models.IntegerField()),
                ('rafael', models.IntegerField()),
            ],
        ),
    ]