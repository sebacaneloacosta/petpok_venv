# Generated by Django 5.0.6 on 2024-07-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.CharField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
            ],
        ),
    ]