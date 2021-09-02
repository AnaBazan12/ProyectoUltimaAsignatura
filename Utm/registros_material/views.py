from django.shortcuts import get_object_or_404, render
from .models import Materiales
from .forms import Materialesforms
from django.contrib import messages
# Create your views here.
def noexiste(request):
    return render(request,"registros_material/404.html")
def principal(request):
    return render(request,"registros_material/inicio.html")

def registrado (request):
    return render (request, "registros_material/registrados.html")

def registrar(request):
    if request.method == 'POST':
        form=Materialesforms(request.POST)
        if form.is_valid():
            matricula=request.POST['matricula']
            nombre_alumno=request.POST['nombre_alumno']
            carrera=request.POST['carrera']
            material=request.POST['material']
            form=Materiales(matricula=matricula, nombre_alumno=nombre_alumno, carrera=carrera, material=material)
            form.save()
            mat=Materiales.objects.all()
            return render(request,'registros_material/adminstrador.html',{'mat':mat})
        else:
            messages.error(request,"Error al procesar el formulario")
    form=Materialesforms()
    return render (request,'registros_material/registrados.html',{'form':form})
    

def admin1 (request):
    mat=Materiales.objects.all()
    return render (request,"registros_material/adminstrador.html",{'mat':mat})

def edicion(request,id):
    mat=Materiales.objects.get(id=id)
    return render(request,"registros_material/editar.html",{'mat':mat})

def editar (request, id):
    materiales=get_object_or_404(Materiales, id=id)
    form = Materialesforms(request.POST, instance=materiales)
    if form.is_valid():
        matricula=request.POST['matricula']
        nombre_alumno=request.POST['nombre_alumno']
        carrera=request.POST['carrera']
        material=request.POST['material']
        form.save()
        mat=Materiales.objects.all()
        return render(request,'registros_material/adminstrador.html',{'mat':mat})
    else:
        messages.error(request, "Error al procesar el formulario")
    form=Materialesforms()
    return render (request,'registros_material/inicio.html',{'form': form})


def eliminar (request,id,
    confirmacion = 'registros_material/eliminar.html'):
    materiales= get_object_or_404(Materiales, id=id)
    if request.method=='POST':
        materiales.delete()
        mat=Materiales.objects.all()
        return render(request,"registros_material/adminstrador.html",{'mat':mat})
    return render (request,confirmacion, {'object':materiales})




