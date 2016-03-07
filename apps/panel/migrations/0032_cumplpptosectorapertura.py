# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0030_detallecalculo_cadena'),
        ('panel', '0031_tendenciageneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='CumplPptoSectorApertura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel2', models.CharField(max_length=50)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cumplimiento', models.FloatField()),
                ('descuento', models.FloatField()),
                ('sector', models.ForeignKey(to='maestros.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
