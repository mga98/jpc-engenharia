from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField('Título', max_length=50)
    slug = models.SlugField(unique=True)
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    author = models.ForeignKey(
        User, verbose_name='Autor', on_delete=models.SET_NULL, null=True
    )
    thumbnail = models.ImageField(
        'Foto de capa',
        upload_to='projects/cover/%Y/%m/%d/',
        blank=True,
        default='',
    )

    def __str__(self):
        return self.title


class Pictures(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True
    )
    image = models.FileField(
        upload_to='projects/images/', blank=True, default=''
    )
