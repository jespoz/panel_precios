# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0003_a900_konp_marm'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioKilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lista', models.CharField(max_length=2)),
                ('material', models.CharField(max_length=50)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('precio', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
