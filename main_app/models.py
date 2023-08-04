from django.db import models
from django.urls import reverse

WATER = (
    ("I", "Infrequent"),
    ("R", "Regular"),
    ("F", "Frequent"),
)

class Soil(models.Model):
  soil_type = models.CharField(max_length=50)
  benefits = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('soils_detail', kwargs={'pk': self.id})



class Plant(models.Model):  
    name = models.CharField(max_length=100)
    habit = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    growth = models.IntegerField()

    soils = models.ManyToManyField(Soil)


    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"plant_id": self.id})


class Watering(models.Model):
        water_required = models.CharField(max_length=1, choices=WATER, default=WATER[0][0])

        plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.get_water_required_display()} "

