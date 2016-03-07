# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0030_detallecalculo_cadena'),
        ('panel', '0028_aperturasectorgeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilos_real', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('ppto', models.FloatField()),
                ('cumplimiento', models.FloatField()),
                ('diferencia', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sector', models.ForeignKey(to='maestros.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
