# Generated by Django 5.0.6 on 2024-07-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_petpokets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
