from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    habit = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    growth = models.IntegerField()

    def __str__(self):
       return self.name