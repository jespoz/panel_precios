# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0012_cargaventa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecalculo',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='detallecalculo',
            name='subtipo',
        ),
        migrations.DeleteModel(
            name='DetalleCalculo',
        ),
    ]
