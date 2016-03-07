# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0025_tipogeneral'),
    ]

    operations = [
        migrations.AddField(
            model_name='cumplpptosectorgeneral',
            name='ppto',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cumplpptotipoclientegeneral',
            name='ppto',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
    ]
