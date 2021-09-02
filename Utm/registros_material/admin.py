from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Materiales
from .models import Profesores
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('matricula','nombre_alumno','carrera')
    search_field=('matricula','nombre_alumno','carrera')
    date_hierarchy= 'created'
    list_filter = ('material','carrera')
admin.site.register(Materiales,AdministrarModelo)

class AdministrarModeloProf(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('Nombre','Laboratorio','Numero')
    search_field=('Matricula','Nombre','Laboratorio')
    date_hierarchy= 'created'
    list_filter = ('Laboratorio','Numero')
admin.site.register(Profesores,AdministrarModeloProf)  