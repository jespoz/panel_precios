# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0025_auto_20160122_1409'),
        ('panel', '0016_auto_20160125_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='AperturaZonaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('zona', models.ForeignKey(to='maestros.ZonaVenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
