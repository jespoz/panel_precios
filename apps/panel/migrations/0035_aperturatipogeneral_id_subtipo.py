# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0034_aperturasectorgeneral_id_nivel2'),
    ]

    operations = [
        migrations.AddField(
            model_name='aperturatipogeneral',
            name='id_subtipo',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
