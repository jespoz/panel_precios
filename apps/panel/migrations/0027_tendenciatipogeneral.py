# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0026_auto_20160125_1643'),
        ('panel', '0026_auto_20160126_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='TendenciaTipoGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(default=b'', max_length=20, null=True)),
                ('descuento', models.FloatField()),
                ('tipo', models.ForeignKey(to='maestros.TipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
