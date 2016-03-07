# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0026_auto_20160125_1643'),
        ('panel', '0024_aperturatipogeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kilos_real', models.FloatField()),
                ('kilos_proy', models.FloatField()),
                ('ppto', models.FloatField()),
                ('cumplimiento', models.FloatField()),
                ('diferencia', models.FloatField(default=0, null=True)),
                ('descuento', models.FloatField()),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('tipo', models.ForeignKey(to='maestros.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
