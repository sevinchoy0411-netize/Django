from django.db import models

# Create your models here.

class Teacher(models.Model):
    ism = models.CharField(max_length=200)
    yonalish = models.CharField(max_length=150)