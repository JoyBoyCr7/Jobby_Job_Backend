from django.db import models

# Create your models here.
class Job(models.Model):
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    # brand_image = models.CharField()
    description = models.CharField()
    interest_level = models.IntegerField()
    application_date = models.DateField()

