# Generated by Django 5.0.6 on 2024-06-11 19:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_paciente_prevision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico',
            old_name='rut',
            new_name='rut_medico',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='nombreCompleto',
            new_name='nombrepa',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='rut',
            new_name='rut_paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='medico',
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.paciente')),
            ],
        ),
        migrations.DeleteModel(
            name='Horas',
        ),
    ]
