# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0014_detallecalculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('codigo', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('sector', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
