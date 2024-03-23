from django.db import models

# Create your models here.
class Personaje(models.Model):
    vidas = models.IntegerField()