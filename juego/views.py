from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'menu/index.html')

def juego(request):
    palabra = {"palabra":"ramon", "categoria":"nombres", "frase":"personaje del chavo"}
    return render(request, 'juegazo/ahorquitos.html', {'palabra': palabra})

