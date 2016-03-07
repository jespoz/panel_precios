# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OficinaVenta',
            fields=[
                ('codigo', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('oficina', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Oficina de Venta',
                'verbose_name_plural': 'Oficina de Ventas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubtipoCliente',
            fields=[
                ('codigo', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('subtipo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subtipo cliente',
                'verbose_name_plural': 'Subtipo clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Cliente',
                'verbose_name_plural': 'Tipo de Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZonaVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zona', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Zona de Venta',
                'verbose_name_plural': 'Zona de Ventas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subtipocliente',
            name='tipocliente',
            field=models.ForeignKey(to='maestros.TipoCliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oficinaventa',
            name='zona',
            field=models.ForeignKey(to='maestros.ZonaVenta'),
            preserve_default=True,
        ),
    ]
