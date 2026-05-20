from django.db import models

# Create your models here.

class Student(models.Model):
    ism = models.CharField(max_length=200)
    yosh = models.IntegerField()
    yonalish = models.CharField(max_length=150)
    group = models.CharField(max_length=150)

    def __str__(self):
        return f"Talaba-{self.ism}"