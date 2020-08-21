from django.db import models
from core.models import User


class Blog(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    image_url = models.URLField('Imagem')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
