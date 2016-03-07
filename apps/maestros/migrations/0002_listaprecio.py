# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaPrecio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lista', models.CharField(max_length=2)),
                ('oficina', models.ForeignKey(to='maestros.OficinaVenta')),
                ('subtipo', models.ForeignKey(to='maestros.SubtipoCliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
