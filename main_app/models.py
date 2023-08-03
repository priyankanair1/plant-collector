from django.db import models
from django.urls import reverse

WATER = (
    ("I", "Infrequent"),
    ("R", "Regular"),
    ("F", "Frequent"),
)


class Plant(models.Model):  
    name = models.CharField(max_length=100)
    habit = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    growth = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"plant_id": self.id})


class Watering(models.Model):
        water_required = models.CharField(max_length=1, choices=WATER, default=WATER[0][0])

        plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.get_water_required_display()} "

