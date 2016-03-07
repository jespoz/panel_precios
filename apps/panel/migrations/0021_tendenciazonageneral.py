# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0026_auto_20160125_1643'),
        ('panel', '0020_zonageneral_diferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='TendenciaZonaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('descuento', models.FloatField()),
                ('zona', models.ForeignKey(to='maestros.ZonaVenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
