# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0015_aperturazonageneral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aperturazonageneral',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='aperturazonageneral',
            name='zona',
        ),
        migrations.DeleteModel(
            name='AperturaZonaGeneral',
        ),
    ]
