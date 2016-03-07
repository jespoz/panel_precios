# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0005_a900_paso'),
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
                ('nivel2', models.CharField(max_length=150)),
                ('sector', models.CharField(max_length=50)),
                ('unidades', models.FloatField()),
                ('kilos', models.FloatField()),
                ('netos', models.FloatField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('subtipo', models.ForeignKey(to='maestros.SubtipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
