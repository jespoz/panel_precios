# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0044_auto_20160202_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablasaperturas',
            name='id_nivel2',
            field=models.CharField(default=b'', max_length=100, null=True),
        ),
    ]
