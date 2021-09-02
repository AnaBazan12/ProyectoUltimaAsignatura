from django.db import models

class Materiales(models.Model): 
    id = models.AutoField(primary_key=True,verbose_name="Id")
    matricula=models.CharField(default='',max_length=20,verbose_name="Matricula")
    nombre_alumno=models.CharField(default='',max_length=50,verbose_name="Nombre del alumno")
    carrera=models.CharField(default='',max_length=20,verbose_name="Carrera")
    material=models.TextField(default='',verbose_name="Materiales")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        ordering = ["created"]

    def __str__(self):
        return self.nombre_alumno


class Profesores(models.Model):
    Nombre=models.CharField(default='',max_length=60,verbose_name="Nombre del Encargado")
    Grado=models.CharField(default='',max_length=60,verbose_name="Grado de estudio del encargado")
    Matricula=models.IntegerField(verbose_name="Matricula del encargado")
    Laboratorio=models.CharField(default='',max_length=60,verbose_name="Nombre del area del laboratorio")
    Numero=models.IntegerField(verbose_name="Numero del laboratorio")
    imagen=models.ImageField(null=True,upload_to="fotos",verbose_name="imagen del encargado")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["created"]

    def __str__(self):
        return self.Nombre
# Create your models here.
