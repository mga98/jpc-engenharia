from django.db import models


class Materials(models.Model):
    material = models.CharField('Material', max_length=50)
    short_description = models.CharField('Descrição', max_length=100)
    sample_picture = models.ImageField(
        'Foto de exemplo',
        upload_to='projects/materials/%Y/%m/%d/',
        blank=True,
        default='',
    )
    stocked = models.BooleanField('Em estoque', default=True)

    def __str__(self):
        return self.material
