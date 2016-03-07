# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0026_auto_20160125_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecalculo',
            name='nivel2_agrupado',
            field=models.CharField(default=b'', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
