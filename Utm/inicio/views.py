from django.shortcuts import render

# Create your views here.
def principal (request):
    return render (request, "inicio/inicio.html")

def registrado (request):
    return render(request,"inicio/registrados.html") 

def admin1 (request):
    return render (request,"inicio/adminstrador.html")