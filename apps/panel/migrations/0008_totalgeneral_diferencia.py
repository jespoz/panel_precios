# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_cumplpptozonageneral'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalgeneral',
            name='diferencia',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
    ]
