# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0020_presupuestoventas2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuestoventas',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='presupuestoventas',
            name='tipocliente',
        ),
        migrations.DeleteModel(
            name='PresupuestoVentas',
        ),
    ]
