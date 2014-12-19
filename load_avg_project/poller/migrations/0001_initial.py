# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('one_minute', models.FloatField()),
                ('five_minute', models.FloatField()),
                ('fifteen_minute', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
