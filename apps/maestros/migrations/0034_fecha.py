# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0033_konp_paso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('habil', models.IntegerField()),
            ],
        ),
    ]
