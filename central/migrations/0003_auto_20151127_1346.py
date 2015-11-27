# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_auto_20151121_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dueno',
            name='contrasena',
        ),
        migrations.AlterField(
            model_name='dueno',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
