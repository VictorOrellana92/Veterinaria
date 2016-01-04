# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0004_auto_20151127_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialcompra',
            name='gusto_compra',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
