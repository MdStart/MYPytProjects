# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyTaskData', '0002_auto_20150428_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='device_name',
            field=models.CharField(max_length=128, unique=True, null=True, blank=True, verbose_name='device_name'),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='field_of_view',
            field=models.IntegerField(verbose_name='field_of_view'),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='magnification',
            field=models.IntegerField(verbose_name='magnification'),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='range',
            field=models.IntegerField(verbose_name='field_of_view'),
        ),
    ]
