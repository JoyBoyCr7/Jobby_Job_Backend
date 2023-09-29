from django.db import models

# Create your models here.
class Job(models.Model):
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    brand_image = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    interest_level = models.IntegerField()
    application_date = models.DateField()

