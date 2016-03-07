# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0030_detallecalculo_cadena'),
        ('panel', '0032_cumplpptosectorapertura'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablasAperturas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel2', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cadena', models.CharField(max_length=50)),
                ('cod_material', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=150)),
                ('kilos', models.FloatField()),
                ('netos', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('neto_esperado', models.FloatField()),
                ('precio_fact', models.FloatField()),
                ('precio_lista', models.FloatField()),
                ('diferencia', models.FloatField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('sector', models.ForeignKey(to='maestros.Sector')),
                ('subtipo', models.ForeignKey(to='maestros.SubtipoCliente')),
                ('tipo', models.ForeignKey(to='maestros.TipoCliente')),
                ('zona', models.ForeignKey(to='maestros.ZonaVenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
