from django.db import models

# Create your models here.
class Job(models.Model):
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    interest = models.IntegerField()
    aplication = models.DateField()

