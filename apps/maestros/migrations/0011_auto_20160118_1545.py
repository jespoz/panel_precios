# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0010_presupuestoventas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargaventa',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='cargaventa',
            name='subtipo',
        ),
        migrations.DeleteModel(
            name='CargaVenta',
        ),
    ]
