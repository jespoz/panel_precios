# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0011_auto_20160118_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargaVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_local', models.CharField(max_length=50)),
                ('cliente_local', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('factura', models.CharField(max_length=50)),
                ('cod_material', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=150)),
                ('sector', models.CharField(max_length=2)),
                ('marca', models.CharField(max_length=50)),
                ('nivel2', models.CharField(max_length=50)),
                ('nivel3', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('unidades', models.FloatField()),
                ('kilos', models.FloatField()),
                ('netos', models.FloatField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('subtipo', models.ForeignKey(to='maestros.SubtipoCliente')),
                ('tipocliente', models.ForeignKey(to='maestros.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
