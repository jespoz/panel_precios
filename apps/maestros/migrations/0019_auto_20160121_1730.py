# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0018_delete_sector'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sector2',
            new_name='Sector',
        ),
    ]
