from dataclasses import dataclass
from datetime import date
from platform import release
from turtle import title
from xml.dom.minidom import AttributeList
from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()