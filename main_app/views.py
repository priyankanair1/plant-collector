from django.shortcuts import render
from .models import Plant



# Create your views here.
# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")

def about(request):

  return render(request, 'about.html')


def plants_index(request):
    plants = Plant.objects.all() 
    return render(request, 'plants/index.html', 
    { 
        'plants': plants 
    }
)
def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  return render(request, 'plants/detail.html', { 'plant': plant })