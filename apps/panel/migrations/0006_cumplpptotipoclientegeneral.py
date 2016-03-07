# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_cumplpptosectorgeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='CumplPptoTipoClienteGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('cumplimiento', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
