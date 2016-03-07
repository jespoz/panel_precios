# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0030_detallecalculo_cadena'),
        ('panel', '0029_sectorgeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='TendenciaSectorGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(default=b'', max_length=20, null=True)),
                ('descuento', models.FloatField()),
                ('sector', models.ForeignKey(to='maestros.Sector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
