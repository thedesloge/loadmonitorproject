# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0003_auto_20141216_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadavgsample',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
