# Generated by Django 5.0.6 on 2024-06-03 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrec', models.CharField(max_length=100)),
                ('motivo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('nombrem', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nombreCompleto', models.CharField(max_length=80)),
                ('rut', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('especialidad', models.CharField(max_length=100)),
                ('prevision', models.CharField(max_length=60)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prevision_paciente', models.CharField(max_length=60)),
                ('especialidad', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.paciente')),
            ],
        ),
    ]
