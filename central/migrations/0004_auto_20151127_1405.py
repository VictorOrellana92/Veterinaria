# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0003_auto_20151127_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veterinario',
            name='contrasena',
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
