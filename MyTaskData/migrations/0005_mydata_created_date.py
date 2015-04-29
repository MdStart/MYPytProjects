# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyTaskData', '0004_auto_20150429_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydata',
            name='created_date',
            field=models.DateField(verbose_name='created_date', default=datetime.datetime(2015, 4, 29, 17, 2, 25, 429778, tzinfo=utc)),
        ),
    ]
