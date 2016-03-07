# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0029_auto_20160127_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecalculo',
            name='cadena',
            field=models.CharField(default=b'', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
