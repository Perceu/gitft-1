from operator import mod
from pyexpat import model
from tkinter import image_names
from django import views
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tag_name


class Fotos(models.Model):
    imagem = models.ImageField(upload_to='fotos')
    descricao = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100, default='3 minutos')
    tags = models.ManyToManyField(Tags)
    views = models.IntegerField()
    publisher = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.descricao