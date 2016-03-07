# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0017_aperturazonageneral'),
    ]

    operations = [
        migrations.AddField(
            model_name='cumplpptozonageneral',
            name='ppto',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
    ]
