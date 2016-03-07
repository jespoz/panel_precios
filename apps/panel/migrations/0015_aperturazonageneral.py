# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0025_auto_20160122_1409'),
        ('panel', '0014_auto_20160125_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='AperturaZonaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('zona', models.ForeignKey(to='maestros.ZonaVenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
