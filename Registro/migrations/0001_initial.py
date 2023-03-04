# Generated by Django 4.1.7 on 2023-03-03 23:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afinidad_Magicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afinidadMagica', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grimorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20)),
                ('trebol', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('identificacion', models.CharField(max_length=10)),
                ('edad', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('status', models.BinaryField(default=False)),
                ('afinidadMagica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.afinidad_magicas')),
                ('grimorio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.grimorios')),
            ],
        ),
    ]
