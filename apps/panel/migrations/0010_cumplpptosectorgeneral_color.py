# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_partdifsectorgeneral_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='cumplpptosectorgeneral',
            name='color',
            field=models.CharField(default=b'', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
