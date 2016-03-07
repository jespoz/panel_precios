# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartDifGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sector', models.CharField(max_length=50)),
                ('diferencia', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
