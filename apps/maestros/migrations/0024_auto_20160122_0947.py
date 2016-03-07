# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0023_detallecalculo2'),
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
        migrations.RemoveField(
            model_name='detallecalculo',
            name='tipocliente',
        ),
        migrations.DeleteModel(
            name='DetalleCalculo',
        ),
    ]
