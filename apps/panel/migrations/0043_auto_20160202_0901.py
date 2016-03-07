# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0042_sectorgeneral_cumpl_netos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cumplpptosectorgeneral',
            old_name='cumplimiento',
            new_name='cumpl_kilos',
        ),
        migrations.AddField(
            model_name='cumplpptosectorgeneral',
            name='cumpl_netos',
            field=models.FloatField(default=0, null=True),
        ),
    ]
