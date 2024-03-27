import random
from django.shortcuts import render, redirect 
from .diccionario import diccionario_palabras
from django.http import HttpResponse
from .models import Personaje
from unidecode import unidecode


def index(request):
    #Personaje.objects.create(vidas = 7)
    cont_vidas = Personaje.objects.get(id = 1)
    cont_vidas.vidas = 7
    cont_vidas.save()
    return render(request, 'menu/index.html')

contador = 0
correctas = ""

def juego(request):

    global contador
    global correctas

    if request.method == "GET":
        lista_caracter = ["'", '-', ',', '.', ';', '_', '¿', '?', '!', '¡', '#', '@', '$', '%' ]
        cont_vidas = Personaje.objects.get(id = 1)
        cont_vidas.vidas = 7
        cont_vidas.save()
        palabra_aleatoria = random.choice(diccionario_palabras)
        palabra_sin_tilde = unidecode(palabra_aleatoria["palabra"])
        palabra_aleatoria["palabra"] = palabra_sin_tilde
        palabra = palabra_aleatoria["palabra"]
        palabra_sin_espacios = palabra.replace(" ", "")
        aleatorio = random.choice(palabra_sin_espacios)
        print(aleatorio)
        print(len(diccionario_palabras))
        print(palabra_sin_espacios)
        vidas = Personaje.objects.get(id = 1).vidas
        return render(request, 'juegazo/ahorquitos.html', {"palabra":palabra_aleatoria, "caracter": aleatorio, 'vidas': vidas, 'lista_caracter':lista_caracter})
    elif request.method == "POST":
        if "palabra" in request.POST:
            print(request.POST.get("palabra"))
            print(request.POST.get("presionarTeclas"))
            cont_vidas = Personaje.objects.get(id = 1)

            presionarTeclas = request.POST.get("presionarTeclas")
            palabra = request.POST.get("palabra")
            palabra_sin_espacios = palabra.replace(" ", "").lower()
            
            if presionarTeclas not in palabra_sin_espacios:
                cont_vidas.vidas = cont_vidas.vidas - 1
                cont_vidas.save()
                print(cont_vidas.vidas)

            elif presionarTeclas in palabra_sin_espacios:
                if presionarTeclas not in correctas:
                    contador += palabra_sin_espacios.count(presionarTeclas)
                    print(f"palabra sin espacios es: {palabra_sin_espacios}")
                    correctas += presionarTeclas
            print(contador)
            if contador == len(palabra_sin_espacios):
                contador = 0
                correctas = ""
                return redirect('ganar')
            print(f"las vidas actuales son: {cont_vidas.vidas} y el tipo de de dato es {type(cont_vidas.vidas)}")
            cont_vidas = Personaje.objects.get(id = 1)
            if cont_vidas.vidas == 0:
                return redirect('derrota')
        elif "escrito-adivina" in request.POST:
            frase_adivinar = request.POST.get("frase-adivinar")
            frase_adivinar = frase_adivinar.lower()
            usuario_adivina = request.POST.get("escrito-adivina")
            usuario_adivina = usuario_adivina.lower()
            if frase_adivinar == usuario_adivina:
                return redirect('ganar')
            else:
                return redirect('derrota')
            #logica para adivinar

        return HttpResponse(status=204)
    
def ganar(request):
    return render(request, 'juegazo/victoria.html')

def derrota(request):
    print("derrota")
    return render(request, 'juegazo/derrota.html')