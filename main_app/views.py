from django.shortcuts import render
plants = [
  {'name': 'Maple', 'habit': 'Trees', 'description': 'Large, woody plants', 'growth': 40 },
  {'name': 'Lilac', 'habit': 'Shrubs', 'description': 'Smaller woody plants', 'growth': 12},
  {'name': 'Corn', 'habit': 'Grasses', 'description': 'Non-woody plants', 'growth': 5 },
]


# Create your views here.
# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")

def about(request):

  return render(request, 'about.html')


def plants_index(request):
  
  return render(request, 'plants/index.html', {
    'plants': plants
  })
