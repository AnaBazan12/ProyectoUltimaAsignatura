"""Utm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros_material import views as vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vistas.principal, name="inicio"),
    path('noexiste/',vistas.noexiste, name="noexiste"),
    path('registra/',vistas.registrado, name="registrado"),
    path('registrar/',vistas.registrar, name="registro"),
    path('administrados/',vistas.admin1, name="administrado"),
    path('eliminar/<int:id>/',vistas.eliminar, name="Eliminar"),
    path('consulta/<int:id>',vistas.edicion,name="edicion"),
    path('editar/<int:id>/',vistas.editar,name="editar"), 
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)