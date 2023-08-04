from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Soil
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
    id_list = plant.soils.all().values_list('id')
    soils_plant_doesnt_have = Soil.objects.exclude(id__in=id_list)
    watering_form = WateringForm()
    print (plant.watering_set.all())
    return render(
        request, "plants/detail.html", {"plant": plant, "watering_form": watering_form, 'soils': soils_plant_doesnt_have
  })
    


def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
        return redirect("detail", plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'habit', 'description', 'growth']



class PlantUpdate(UpdateView):
    model = Plant
    fields = ["habit", "description", "growth"]


class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants"

class SoilList(ListView):
  model = Soil

class SoilDetail(DetailView):
  model = Soil

class SoilCreate(CreateView):
  model = Soil
  fields = '__all__'

class SoilUpdate(UpdateView):
  model = Soil
  fields = ['soil_type', 'benefits']

class SoilDelete(DeleteView):
  model = Soil
  success_url = '/soils'


def assoc_soil(request, plant_id, soil_id):
  Plant.objects.get(id=plant_id).soils.add(soil_id)
  return redirect('detail', plant_id=plant_id)

def unassoc_soil(request, plant_id, soil_id):
  Plant.objects.get(id=plant_id).soils.remove(soil_id)
  return redirect('detail', plant_id=plant_id)
