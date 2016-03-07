# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0002_listaprecio'),
    ]

    operations = [
        migrations.CreateModel(
            name='A900',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lista', models.CharField(max_length=2)),
                ('material', models.CharField(max_length=50)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('registro', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KONP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registro', models.CharField(max_length=50)),
                ('importe', models.FloatField(default=0)),
                ('um', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MARM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=50)),
                ('um', models.CharField(max_length=10)),
                ('contador', models.FloatField(default=0)),
                ('denominador', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
