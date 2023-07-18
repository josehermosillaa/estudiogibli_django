import requests
from django.shortcuts import render, HttpResponse
from .models import Pelicula
# Create your views here.

def index_view(request):
    return HttpResponse("<h1> Estudio Gibli </h1>")

def load_view(request):
    url = "https://studio-ghibli-films-api.herokuapp.com/api"
    response = requests.get(url)

    if response.status_code == 200:
        # data = response.json()
        # keys = response.json().keys()
        values = response.json().values()
        for value in values:
            Pelicula.objects.update_or_create(
                title=value["title"],
                poster=value["poster"],
                genre=value["genre"],
                rating=value["rating"],
                release=value["release"],
                director=value["director"]
            )
        return HttpResponse("<h1>los datos se cargaron correctamente</h1>")
    return HttpResponse("<h1>los datos no se cargaron correctamente</h1>")
    