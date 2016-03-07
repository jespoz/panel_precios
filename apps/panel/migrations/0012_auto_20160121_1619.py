# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_auto_20160121_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalgeneral',
            name='cumpl_netos',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='totalgeneral',
            name='netos_ppto',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='totalgeneral',
            name='netos_real',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
    ]
