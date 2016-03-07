# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0026_auto_20160125_1643'),
        ('panel', '0018_cumplpptozonageneral_ppto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilos_real', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('ppto', models.FloatField()),
                ('cumplimiento', models.FloatField()),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('zona', models.ForeignKey(to='maestros.ZonaVenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
