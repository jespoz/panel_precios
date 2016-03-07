# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'panel', '0001_initial'), (b'panel', '0002_partdifgeneral'), (b'panel', '0003_auto_20160119_1048'), (b'panel', '0004_partdifzonageneral'), (b'panel', '0005_cumplpptosectorgeneral'), (b'panel', '0006_cumplpptotipoclientegeneral'), (b'panel', '0007_cumplpptozonageneral'), (b'panel', '0008_totalgeneral_diferencia'), (b'panel', '0009_partdifsectorgeneral_color'), (b'panel', '0010_cumplpptosectorgeneral_color'), (b'panel', '0011_auto_20160121_1545'), (b'panel', '0012_auto_20160121_1619'), (b'panel', '0013_cumplpptosectorgeneral_descuento'), (b'panel', '0014_auto_20160125_1234'), (b'panel', '0015_aperturazonageneral'), (b'panel', '0016_auto_20160125_1447'), (b'panel', '0017_aperturazonageneral'), (b'panel', '0018_cumplpptozonageneral_ppto'), (b'panel', '0019_zonageneral'), (b'panel', '0020_zonageneral_diferencia'), (b'panel', '0021_tendenciazonageneral'), (b'panel', '0022_auto_20160126_1326'), (b'panel', '0023_tendenciazonageneral'), (b'panel', '0024_aperturatipogeneral'), (b'panel', '0025_tipogeneral'), (b'panel', '0026_auto_20160126_1524'), (b'panel', '0027_tendenciatipogeneral'), (b'panel', '0028_aperturasectorgeneral'), (b'panel', '0029_sectorgeneral'), (b'panel', '0030_tendenciasectorgeneral'), (b'panel', '0031_tendenciageneral'), (b'panel', '0032_cumplpptosectorapertura'), (b'panel', '0033_tablasaperturas'), (b'panel', '0034_aperturasectorgeneral_id_nivel2'), (b'panel', '0035_aperturatipogeneral_id_subtipo'), (b'panel', '0036_auto_20160201_1558'), (b'panel', '0037_tablasaperturas'), (b'panel', '0038_auto_20160201_1604'), (b'panel', '0039_auto_20160201_1605'), (b'panel', '0040_tablasaperturas'), (b'panel', '0041_auto_20160202_0854'), (b'panel', '0042_sectorgeneral_cumpl_netos'), (b'panel', '0043_auto_20160202_0901'), (b'panel', '0044_auto_20160202_1028'), (b'panel', '0045_tablasaperturas_id_nivel2'), (b'panel', '0046_auto_20160215_1151'), (b'panel', '0047_auto_20160215_1154'), (b'panel', '0048_auto_20160215_1702'), (b'panel', '0049_auto_20160215_1716'), (b'panel', '0050_auto_20160216_1635')]

    initial = True

    dependencies = [
        ('maestros', '0001_squashed_0035_actualizacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('descuento', models.FloatField()),
                ('precio_lista', models.FloatField()),
                ('precio_real', models.FloatField()),
                ('kilos_real', models.FloatField()),
                ('kilos_ppto', models.FloatField()),
                ('cumpl_kilos', models.FloatField()),
                ('diferencia', models.FloatField(default=0, null=True)),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
                ('netos_ppto', models.FloatField(default=0, null=True)),
                ('netos_real', models.FloatField(default=0, null=True)),
                ('kilos_proy', models.FloatField(default=0, null=True)),
                ('netos_proy', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartDifSectorGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sector', models.CharField(max_length=50)),
                ('diferencia', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PartDifTipoClienteGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('diferencia', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PartDifZonaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('zona', models.CharField(max_length=50)),
                ('diferencia', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CumplPptoSectorGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sector', models.CharField(max_length=50)),
                ('cumpl_kilos', models.FloatField()),
                ('descuento', models.FloatField(default=0, null=True)),
                ('ppto', models.FloatField(default=0, null=True)),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CumplPptoTipoClienteGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('cumpl_kilos', models.FloatField()),
                ('descuento', models.FloatField(default=0, null=True)),
                ('ppto', models.FloatField(default=0, null=True)),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CumplPptoZonaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('zona', models.CharField(max_length=50)),
                ('cumpl_kilos', models.FloatField()),
                ('descuento', models.FloatField(default=0, null=True)),
                ('ppto', models.FloatField(default=0, null=True)),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AperturaZonaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.OficinaVenta')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.ZonaVenta')),
            ],
        ),
        migrations.CreateModel(
            name='ZonaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilos_real', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('ppto', models.FloatField()),
                ('cumpl_kilos', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.ZonaVenta')),
                ('diferencia', models.FloatField(default=0, null=True)),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TendenciaZonaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default=b'', max_length=20, null=True)),
                ('descuento', models.FloatField()),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.ZonaVenta')),
                ('mes', models.IntegerField(default=0, null=True)),
                ('year', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AperturaTipoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtipo', models.CharField(max_length=100)),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
                ('id_subtipo', models.CharField(default=b'', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilos_real', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('ppto', models.FloatField()),
                ('cumpl_kilos', models.FloatField()),
                ('diferencia', models.FloatField(default=0, null=True)),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TendenciaTipoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default=b'', max_length=20, null=True)),
                ('descuento', models.FloatField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
                ('mes', models.IntegerField(default=0, null=True)),
                ('year', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AperturaSectorGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel2', models.CharField(max_length=100)),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
                ('id_nivel2', models.CharField(default=b'', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectorGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilos_real', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('ppto', models.FloatField()),
                ('cumpl_kilos', models.FloatField()),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
                ('cumpl_netos', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TendenciaSectorGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default=b'', max_length=20, null=True)),
                ('descuento', models.FloatField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
                ('mes', models.IntegerField(default=0, null=True)),
                ('year', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TendenciaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=20)),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField(default=0, null=True)),
                ('year', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CumplPptoSectorApertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel2', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cumplimiento', models.FloatField()),
                ('descuento', models.FloatField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
            ],
        ),
        migrations.CreateModel(
            name='TablasAperturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel2', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cadena_desc', models.CharField(max_length=50)),
                ('cod_material', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=150)),
                ('kilos', models.FloatField()),
                ('netos', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('neto_esperado', models.FloatField()),
                ('precio_fact', models.FloatField()),
                ('precio_lista', models.FloatField()),
                ('diferencia', models.FloatField()),
                ('cadena', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maestros.Cadena')),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.OficinaVenta')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.Sector')),
                ('subtipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.SubtipoCliente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.TipoCliente')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestros.ZonaVenta')),
                ('id_nivel2', models.CharField(default=b'', max_length=100, null=True)),
            ],
        ),
    ]
