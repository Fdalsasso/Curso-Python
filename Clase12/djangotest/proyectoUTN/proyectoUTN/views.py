from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from .models import Database


def hola(request):
    return HttpResponse("Bienvenido al sistema Proyecto-UTN")

# def bienvenida(request):

#     archivo_html=open("C:/Users/Rodrigo/Desktop/Django-UTN/proyectoUTN/proyectoUTN/mytemplates/index.html")
#     html=Template(archivo_html.read())
#     archivo_html.close()
#     contexto=Context()
#     documento_final=html.render(contexto)
#     return HttpResponse(documento_final)

# def bienvenida(request):

#     documento= loader.get_template("index.html")
#     documento_final=documento.render()
#     return HttpResponse(documento_final)

def bienvenida(request):
    nombre="Rodrigo" #Contexto es el tercer párametro
    return render(request, "index.html", {"nombre":nombre})

def saludo_personalizado(request, nombre, apellido,edad):

    anio_nacimiento= 2022-edad
    listado_lenguajes=["Python", "Java", "C", "Javascript"]

    return render(request,"sp.html", {"nombre": nombre, "apellido": apellido, "anio": anio_nacimiento, "lenguajes": listado_lenguajes})

def vistaformulario(request):
    return render(request, "form.html")

def recibiendoget(request):
    nombre_usuario=request.GET["nombre"]
    apellido_usuario=request.GET["apellido"]
    return render(request, "index.html", {"nombre":nombre_usuario, "apellido":apellido_usuario})

def formulario_perro(request):
    return render(request, "formulario.html")

def hija(request):
    return render(request, "hija.html")

def todos_medicos(request):
    db=Database()
    info=db.all_users()
    return render(request, "medicos.html", {"info": info})






