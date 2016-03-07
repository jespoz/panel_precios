# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0030_tendenciasectorgeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='TendenciaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=20)),
                ('descuento', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
