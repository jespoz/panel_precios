# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0017_sector2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sector',
        ),
    ]
