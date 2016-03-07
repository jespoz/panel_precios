# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0008_detallecalculo_lista'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecalculo',
            name='mes',
            field=models.CharField(default=b'', max_length=2, null=True),
            preserve_default=True,
        ),
    ]
