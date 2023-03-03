from operator import truediv
from django.db import models

# Create your models here.


class Vitrola(models.Model):
    artist = models.CharField(max_length=60)
    titulo = models.CharField(max_length=100)
    track = models.FileField(upload_to='documents/')

class WaitList(models.Model):
    artist = models.CharField(max_length=60)
    titulo = models.CharField(max_length=100)
    track = models.FileField(upload_to='documents/')