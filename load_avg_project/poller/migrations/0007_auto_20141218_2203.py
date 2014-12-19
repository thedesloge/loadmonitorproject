# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0006_loadavgevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadavgevent',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 18, 22, 2, 56, 374467)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loadavgevent',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
