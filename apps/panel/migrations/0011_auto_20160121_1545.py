# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_cumplpptosectorgeneral_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cumplpptosectorgeneral',
            name='color',
        ),
        migrations.RemoveField(
            model_name='partdifsectorgeneral',
            name='color',
        ),
    ]
