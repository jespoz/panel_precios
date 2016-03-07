# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_totalgeneral_diferencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='partdifsectorgeneral',
            name='color',
            field=models.CharField(default=b'', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
