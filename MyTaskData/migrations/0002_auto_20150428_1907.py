# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyTaskData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('device_name', models.CharField(blank=True, null=True, unique=True, verbose_name='id', max_length=128)),
                ('magnification', models.IntegerField()),
                ('field_of_view', models.IntegerField()),
                ('range', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyFields',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('did', models.CharField(blank=True, null=True, unique=True, verbose_name='id', max_length=128)),
                ('label', models.CharField(blank=True, null=True, unique=True, verbose_name='id', max_length=128)),
                ('type', models.CharField(blank=True, null=True, unique=True, verbose_name='id', max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='taskdata',
            name='device_name',
        ),
        migrations.RemoveField(
            model_name='taskdata',
            name='field_of_view',
        ),
        migrations.RemoveField(
            model_name='taskdata',
            name='magnification',
        ),
        migrations.RemoveField(
            model_name='taskdata',
            name='range',
        ),
        migrations.AddField(
            model_name='taskdata',
            name='data',
            field=models.ForeignKey(to='MyTaskData.MyData', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='taskdata',
            name='fields',
            field=models.ForeignKey(to='MyTaskData.MyFields', null=True, blank=True),
        ),
    ]
