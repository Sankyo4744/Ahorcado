import random
from django.shortcuts import render 
from .diccionario import diccionario_palabras
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'menu/index.html')

def juego(request):
    vidas = 7
    if request.method == "GET":
        
        palabra_aleatoria = random.choice(diccionario_palabras)
        palabra = palabra_aleatoria["palabra"]
        palabra_sin_espacios = palabra.replace(" ", "")
        aleatorio = random.choice(palabra_sin_espacios)
        print(aleatorio)
        print(len(diccionario_palabras))
        return render(request, 'juegazo/ahorquitos.html', {"palabra":palabra_aleatoria, "caracter": aleatorio})
    elif request.method == "POST":
        print(request.POST.get("palabra"))
        print(request.POST.get("presionarTeclas"))

        presionarTeclas = request.POST.get("presionarTeclas")
        palabra = request.POST.get("palabra")
        
        if presionarTeclas not in palabra:
            vidas = vidas - 1
        print(vidas)

        return HttpResponse(status=204)

