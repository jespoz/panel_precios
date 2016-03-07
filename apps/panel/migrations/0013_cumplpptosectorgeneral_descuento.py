# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0012_auto_20160121_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='cumplpptosectorgeneral',
            name='descuento',
            field=models.FloatField(default=0, null=True),
            preserve_default=True,
        ),
    ]
