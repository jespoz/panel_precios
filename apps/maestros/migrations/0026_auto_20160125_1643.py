# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0025_auto_20160122_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecalculo',
            name='year',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
