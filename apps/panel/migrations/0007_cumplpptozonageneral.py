# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_cumplpptotipoclientegeneral'),
    ]

    operations = [
        migrations.CreateModel(
            name='CumplPptoZonaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('zona', models.CharField(max_length=50)),
                ('cumplimiento', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
