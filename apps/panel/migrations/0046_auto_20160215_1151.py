# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0045_tablasaperturas_id_nivel2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tendenciageneral',
            name='mes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='tendenciageneral',
            name='year',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
