# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0002_auto_20141216_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadavgsample',
            name='timestamp',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
