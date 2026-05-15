from django.db import models

# Create your models here.

class Teacher(models.Model):
    ismi = models.CharField(max_length=200)
    yonalishi = models.CharField(max_length=150)