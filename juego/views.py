import random
from django.shortcuts import render, redirect 
from .diccionario import diccionario_palabras
from django.http import HttpResponse
from .models import Personaje
from unidecode import unidecode

#vista para el menu, se declaran las variables para acceder al dato mediante el id en la base de datos y se restablece el valor de vidas a 7
def index(request):
    #Personaje.objects.create(vidas = 7)
    cont_vidas = Personaje.objects.get(id = 1)
    cont_vidas.vidas = 7
    cont_vidas.save()
    return render(request, 'menu/index.html')

#se declaran las varibles para guardar la informacion de los caracteres correctos y la cantidad de letras correctas
contador = 0
correctas = ""
incorrectas = ""

def juego(request):

    global contador
    global correctas
    global incorrectas
    #se crea el condicional para verificar si el metodo de la peticion es get
    if request.method == "GET":
        lista_caracter = ["'", '-', ',', '.', ';', '_', '¿', '?', '!', '¡', '#', '@', '$', '%' ]
        cont_vidas = Personaje.objects.get(id = 1)
        cont_vidas.vidas = 7
        cont_vidas.save()
        palabra_aleatoria = random.choice(diccionario_palabras)
        palabra_sin_tilde = unidecode(palabra_aleatoria["palabra"])
        for caracter in lista_caracter:
            palabra_sin_tilde = palabra_sin_tilde.replace(caracter, "")
        #al diccionario de palabra_aleatoria se le asigna al valor de palabra_sin_tilde a la clave palabra
        palabra_aleatoria["palabra"] = palabra_sin_tilde
        palabra = palabra_aleatoria["palabra"]
        palabra_sin_espacios = palabra.replace(" ", "")
        aleatorio = random.choice(palabra_sin_espacios)
        print(aleatorio)
        print(len(diccionario_palabras))
        print(palabra_sin_espacios)
        vidas = Personaje.objects.get(id = 1).vidas
        return render(request, 'juegazo/ahorquitos.html', {"palabra":palabra_aleatoria, "caracter": aleatorio, 'vidas': vidas, 'lista_caracter':lista_caracter})
    #verifica si el metodo de la peticion es POST cada vez que oprime una tecla
    elif request.method == "POST":
        #condicional para verificar si la clave palabra que esta siendo enviada del formulario (formTeclas) esta en la peticion POST
        if "palabra" in request.POST:
            print(request.POST.get("palabra"))
            print(request.POST.get("presionarTeclas"))
            cont_vidas = Personaje.objects.get(id = 1)

            presionarTeclas = request.POST.get("presionarTeclas")
            palabra = request.POST.get("palabra")
            palabra_sin_espacios = palabra.replace(" ", "").lower()
            
            if presionarTeclas not in palabra_sin_espacios:
                if presionarTeclas not in incorrectas:
                    incorrectas += presionarTeclas
                    cont_vidas.vidas = cont_vidas.vidas - 1
                    cont_vidas.save()
                    print(cont_vidas.vidas)

            elif presionarTeclas in palabra_sin_espacios:
                # es el condicional para sabe si la tecla ya se encuentra en la varible correctas o toca añadirla
                if presionarTeclas not in correctas:
                    #count va a contar cuantas veces estan las teclas correctas
                    contador += palabra_sin_espacios.count(presionarTeclas) 
                    print(f"palabra sin espacios es: {palabra_sin_espacios}")
                    #correctas esta añadiendo las letras correctas en un string
                    correctas += presionarTeclas
            print(contador)
            if contador == len(palabra_sin_espacios):
                contador = 0
                correctas = ""
                incorrectas = ""
                return redirect('ganar')
            print(f"las vidas actuales son: {cont_vidas.vidas} y el tipo de de dato es {type(cont_vidas.vidas)}")
            cont_vidas = Personaje.objects.get(id = 1)
            if cont_vidas.vidas == 0:
                return redirect('derrota')
        #logica para adivinar
        elif "escrito-adivina" in request.POST:
            frase_adivinar = request.POST.get("frase-adivinar")
            frase_adivinar = frase_adivinar.lower()
            usuario_adivina = request.POST.get("escrito-adivina")
            usuario_adivina = usuario_adivina.lower()
            if frase_adivinar == usuario_adivina:
                return redirect('ganar')
            else:
                return redirect('derrota')

        return HttpResponse(status=204)
    
def ganar(request):
    return render(request, 'juegazo/victoria.html')

def derrota(request):
    print("derrota")
    return render(request, 'juegazo/derrota.html')