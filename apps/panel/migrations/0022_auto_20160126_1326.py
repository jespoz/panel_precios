# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0021_tendenciazonageneral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tendenciazonageneral',
            name='zona',
        ),
        migrations.DeleteModel(
            name='TendenciaZonaGeneral',
        ),
    ]
