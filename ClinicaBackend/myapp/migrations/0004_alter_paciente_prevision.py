# Generated by Django 5.0.6 on 2024-06-04 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_paciente_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='prevision',
            field=models.CharField(choices=[('FONASA', 'Fonasa'), ('ISAPRE', 'Isapre'), ('PARTICULAR', 'Particular')], max_length=20),
        ),
    ]
