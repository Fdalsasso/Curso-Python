from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def hola(request):
    return HttpResponse("El primer intento funciona")

# def bienvenida(request):
    
#      archivo_html = open("C:/Users/colo2/OneDrive/Desktop/Curso Python/Clase11/Primer_Intento/Primer_Intento/Templates/index.html")
#      html = Template(archivo_html.read())
#      archivo_html.close()
#      contexto = Context()
#      documento_final = html.render(contexto)

#      return HttpResponse(documento_final)

# def bienvenida(request):
#      documento = loader.get_template("imdex.html")
#      documentoFinal = documento.render()           no me toma el render xd
#      return HttpResponse(documentoFinal)

def bienvenida(request):
    algo = "algo"
    return render(request, "index.html", {"nombre": algo})

def saludo(request, nombre, apellido, anio):
    anioNac = 2022 - anio
    
    lista = []
    return render(request, "index.html", {"nombre": nombre, "apellido": apellido, "anio": anioNac, "nombres": lista})

def vistaFormulario(request):
    return render(request, "form.html")

def recibiendoGet(request):
    nombre_usuario = request.GET["nombre"]
    apellido_usuario = request.GET["apellido"]
    return render(request, "index.html", {"nombre": nombre_usuario, "apellido": apellido_usuario})
