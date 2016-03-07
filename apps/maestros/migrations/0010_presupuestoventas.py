# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0009_detallecalculo_mes'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestoVentas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sector', models.CharField(max_length=2)),
                ('marca', models.CharField(max_length=50)),
                ('nivel2', models.CharField(max_length=50)),
                ('nivel3', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('kilo', models.FloatField()),
                ('neto', models.FloatField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('tipocliente', models.ForeignKey(to='maestros.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
