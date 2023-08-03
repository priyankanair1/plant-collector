from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from .forms import WateringForm


# Create your views here.
# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    print (plant.watering_set.all())
    return render(
        request, "plants/detail.html", {"plant": plant, "watering_form": watering_form}
    )


def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
        return redirect("detail", plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = "__all__"


class PlantUpdate(UpdateView):
    model = Plant
    fields = ["habit", "description", "growth"]


class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants"
