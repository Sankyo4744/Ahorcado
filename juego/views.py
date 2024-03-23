import random
from django.shortcuts import render 
from .diccionario import diccionario_palabras
from django.http import HttpResponse
from .models import Personaje

# Create your views here.

def index(request):
    #Personaje.objects.create(vidas = 7)
    cont_vidas = Personaje.objects.get(id = 1)
    cont_vidas.vidas = 7
    cont_vidas.save()
    return render(request, 'menu/index.html')

def juego(request):

    if request.method == "GET":
        cont_vidas = Personaje.objects.get(id = 1)
        cont_vidas.vidas = 7
        cont_vidas.save()
        palabra_aleatoria = random.choice(diccionario_palabras)
        palabra = palabra_aleatoria["palabra"]
        palabra_sin_espacios = palabra.replace(" ", "")
        aleatorio = random.choice(palabra_sin_espacios)
        print(aleatorio)
        print(len(diccionario_palabras))
        vidas = Personaje.objects.get(id = 1).vidas
        return render(request, 'juegazo/ahorquitos.html', {"palabra":palabra_aleatoria, "caracter": aleatorio, 'vidas': vidas})
    elif request.method == "POST":
        print(request.POST.get("palabra"))
        print(request.POST.get("presionarTeclas"))

        presionarTeclas = request.POST.get("presionarTeclas")
        palabra = request.POST.get("palabra")
        
        
        if presionarTeclas not in palabra:
            cont_vidas = Personaje.objects.get(id = 1)
            cont_vidas.vidas = cont_vidas.vidas - 1
            cont_vidas.save()
            print(cont_vidas.vidas)

            response = HttpResponse(cont_vidas.vidas, status=200)
        return response

