# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TotalGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('descuento', models.FloatField()),
                ('precio_lista', models.FloatField()),
                ('precio_real', models.FloatField()),
                ('kilos_real', models.FloatField()),
                ('kilos_ppto', models.FloatField()),
                ('cumpl_kilos', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
