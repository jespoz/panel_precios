# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0027_detallecalculo_nivel2_agrupado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecalculo',
            name='nivel2',
            field=models.CharField(max_length=50, db_index=True),
            preserve_default=True,
        ),
    ]
