# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0030_detallecalculo_cadena'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel2',
            fields=[
                ('codigo', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('nivel', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
