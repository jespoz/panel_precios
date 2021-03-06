# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0021_auto_20160121_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestoVentas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=50)),
                ('nivel2', models.CharField(max_length=50)),
                ('nivel3', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('kilo', models.FloatField()),
                ('neto', models.FloatField()),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('sector', models.ForeignKey(to='maestros.Sector')),
                ('tipocliente', models.ForeignKey(to='maestros.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='presupuestoventas2',
            name='oficina',
        ),
        migrations.RemoveField(
            model_name='presupuestoventas2',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='presupuestoventas2',
            name='tipocliente',
        ),
        migrations.DeleteModel(
            name='PresupuestoVentas2',
        ),
    ]
