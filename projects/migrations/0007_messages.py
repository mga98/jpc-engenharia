# Generated by Django 4.2 on 2023-04-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_pictures_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('phone', models.CharField(max_length=20, verbose_name='Celular ou Telefone')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail para contato')),
                ('message', models.TextField()),
                ('sended_at', models.DateTimeField(auto_now_add=True, verbose_name='Enviada em')),
                ('read', models.BooleanField(default=False, verbose_name='Lida')),
            ],
        ),
    ]
