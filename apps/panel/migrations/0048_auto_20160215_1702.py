# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0047_auto_20160215_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tendenciageneral',
            name='fecha',
            field=models.DateField(),
        ),
    ]
