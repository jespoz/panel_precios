# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0016_sector_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector2',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('sector', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
