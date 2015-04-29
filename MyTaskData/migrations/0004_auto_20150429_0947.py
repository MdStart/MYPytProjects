# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyTaskData', '0003_auto_20150428_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='device_name',
            field=models.CharField(null=True, blank=True, max_length=128, verbose_name='device_name'),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='field_of_view',
            field=models.CharField(null=True, blank=True, max_length=128, verbose_name='field_of_view'),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='magnification',
            field=models.CharField(null=True, blank=True, max_length=128, verbose_name='magnification'),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='range',
            field=models.CharField(null=True, blank=True, max_length=128, verbose_name='range'),
        ),
    ]
