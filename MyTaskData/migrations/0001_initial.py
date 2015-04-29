# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('device_name', models.CharField(max_length=100)),
                ('magnification', models.IntegerField()),
                ('field_of_view', models.IntegerField()),
                ('range', models.IntegerField()),
            ],
        ),
    ]
