# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0028_auto_20160127_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargaventa',
            name='cadena',
            field=models.CharField(default=b'', max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargaventa',
            name='nivel2_agrupado',
            field=models.CharField(default=b'', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
