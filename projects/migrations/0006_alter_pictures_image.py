# Generated by Django 4.2 on 2023-04-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_pictures_pictures_remove_project_pictures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.FileField(blank=True, default='', upload_to='projects/images/', verbose_name='Fotos do projeto'),
        ),
    ]
