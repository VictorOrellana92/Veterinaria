# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domicilio', models.BooleanField()),
                ('fecha_Atencion', models.DateField()),
                ('temperatura', models.FloatField()),
                ('observaciones', models.TextField()),
                ('diagnostico', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('rut', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=20)),
                ('Tipo_de_Usuario', models.CharField(max_length=1, choices=[(b'C', b'Cliente'), (b'V', b'Veterinario'), (b'A', b'Administrador')])),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creacion', models.DateField(auto_now=True)),
                ('amo', models.ForeignKey(to='central.Dueno')),
                ('clinica', models.ForeignKey(to='central.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField(verbose_name=b'')),
                ('observaciones', models.CharField(max_length=20)),
                ('dueno', models.ForeignKey(to='central.Dueno')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio', models.DateField(auto_now=True)),
                ('clinica', models.ForeignKey(to='central.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('vigencia', models.DurationField()),
                ('capacidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=20)),
                ('Tipo_de_Usuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='plan',
            field=models.ForeignKey(to='central.Plan'),
        ),
        migrations.AddField(
            model_name='historialcompra',
            name='numero_compra',
            field=models.ForeignKey(to='central.OrdenCompra'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='nombre',
            field=models.ForeignKey(to='central.Mascota'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='ficha',
            field=models.ForeignKey(to='central.Ficha'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='veterinario',
            field=models.ForeignKey(to='central.Veterinario'),
        ),
    ]
