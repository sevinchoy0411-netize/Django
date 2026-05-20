from django.db import models

# Create your models here.

class Teacher(models.Model):
    ism = models.CharField(max_length=200)
    yosh = models.IntegerField()
    yonalish = models.CharField(max_length=150)
    tajriba = models.IntegerField()

    def __str__(self):
        return f"Ustoz-{self.ism}"