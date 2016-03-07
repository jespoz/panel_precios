# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'maestros', '0001_initial'), (b'maestros', '0002_listaprecio'), (b'maestros', '0003_a900_konp_marm'), (b'maestros', '0004_preciokilo'), (b'maestros', '0005_a900_paso'), (b'maestros', '0006_cargaventa'), (b'maestros', '0007_detallecalculo'), (b'maestros', '0008_detallecalculo_lista'), (b'maestros', '0009_detallecalculo_mes'), (b'maestros', '0010_presupuestoventas'), (b'maestros', '0011_auto_20160118_1545'), (b'maestros', '0012_cargaventa'), (b'maestros', '0013_auto_20160119_0912'), (b'maestros', '0014_detallecalculo'), (b'maestros', '0015_sector'), (b'maestros', '0016_sector_color'), (b'maestros', '0017_sector2'), (b'maestros', '0018_delete_sector'), (b'maestros', '0019_auto_20160121_1730'), (b'maestros', '0020_presupuestoventas2'), (b'maestros', '0021_auto_20160121_1735'), (b'maestros', '0022_auto_20160121_1739'), (b'maestros', '0023_detallecalculo2'), (b'maestros', '0024_auto_20160122_0947'), (b'maestros', '0025_auto_20160122_1409'), (b'maestros', '0026_auto_20160125_1643'), (b'maestros', '0027_detallecalculo_nivel2_agrupado'), (b'maestros', '0028_auto_20160127_1035'), (b'maestros', '0029_auto_20160127_1105'), (b'maestros', '0030_detallecalculo_cadena'), (b'maestros', '0031_nivel2'), (b'maestros', '0032_cadena'), (b'maestros', '0033_konp_paso'), (b'maestros', '0034_fecha'), (b'maestros', '0035_actualizacion')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OficinaVenta',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('oficina', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Oficina de Venta',
                'verbose_name_plural': 'Oficina de Ventas',
            },
        ),
        migrations.CreateModel(
            name='SubtipoCliente',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subtipo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subtipo cliente',
                'verbose_name_plural': 'Subtipo clientes',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Cliente',
                'verbose_name_plural': 'Tipo de Clientes',
            },
        ),
        migrations.CreateModel(
            name='ZonaVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Zona de Venta',
                'verbose_name_plural': 'Zona de Ventas',
            },
        ),
        migrations.AddField(
            model_name='subtipocliente',
            name='tipocliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente'),
        ),
        migrations.AddField(
            model_name='oficinaventa',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.ZonaVenta'),
        ),
        migrations.CreateModel(
            name='ListaPrecio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.CharField(max_length=2)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.OficinaVenta')),
                ('subtipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.SubtipoCliente')),
            ],
        ),
        migrations.CreateModel(
            name='A900',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.CharField(max_length=2)),
                ('material', models.CharField(max_length=50)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('registro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KONP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=50)),
                ('importe', models.FloatField(default=0)),
                ('um', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MARM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=50)),
                ('um', models.CharField(max_length=10)),
                ('contador', models.FloatField(default=0)),
                ('denominador', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PrecioKilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.CharField(max_length=2)),
                ('material', models.CharField(max_length=50)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('precio', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='A900_Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.CharField(max_length=2)),
                ('material', models.CharField(max_length=50)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('registro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CargaVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.OficinaVenta')),
                ('subtipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.SubtipoCliente')),
                ('tipocliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
                ('cadena', models.CharField(default=b'', max_length=50, null=True)),
                ('nivel2_agrupado', models.CharField(default=b'', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PresupuestoVentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('nivel2', models.CharField(max_length=50)),
                ('nivel3', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('kilo', models.FloatField()),
                ('neto', models.FloatField()),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.OficinaVenta')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
                ('tipocliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCalculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_local', models.CharField(max_length=50)),
                ('cliente_local', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('factura', models.CharField(max_length=50)),
                ('cod_material', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=50)),
                ('nivel2', models.CharField(db_index=True, max_length=50)),
                ('nivel3', models.CharField(max_length=50)),
                ('year', models.IntegerField(db_index=True)),
                ('unidades', models.FloatField()),
                ('kilos', models.FloatField()),
                ('netos', models.FloatField()),
                ('precio_promedio', models.FloatField()),
                ('precio_lista', models.FloatField()),
                ('diferencia', models.FloatField()),
                ('neto_esperado', models.FloatField()),
                ('lista', models.CharField(max_length=2)),
                ('mes', models.CharField(max_length=2)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.OficinaVenta')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
                ('subtipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.SubtipoCliente')),
                ('tipocliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
                ('nivel2_agrupado', models.CharField(default=b'', max_length=50, null=True)),
                ('cadena', models.CharField(default=b'', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel2',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nivel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cadena',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cadena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KONP_Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=50)),
                ('importe', models.FloatField(default=0)),
                ('um', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('habil', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Actualizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
    ]