from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
