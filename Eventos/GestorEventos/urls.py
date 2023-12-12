"""
URL configuration for GestorEventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from GestorEventosApp.views import actualizar_evento, crear_categoria, crear_evento, crear_ubicacion, eliminar_categoria, eliminar_evento, eliminar_ubicacion, lista_categorias, lista_eventos, lista_ubicaciones, login_view, logout, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),

    #Urls para listas}
    path('ubicaciones/', lista_ubicaciones, name='lista_ubicaciones'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('eventos/', lista_eventos, name='lista_eventos'),

    # Urls para crear
    path('crear-evento/', crear_evento, name='crear_evento'),
    path('crear_categoria/',crear_categoria, name='crear_categoria'),
    path('crear_ubicacion/',crear_ubicacion, name='crear_ubicacion'),

    #Urls para eliminar
    path('eventos/<int:evento_id>/eliminar/', eliminar_evento, name='eliminar_evento'),
    path('categorias/<int:categoria_id>/eliminar/', eliminar_categoria, name='eliminar_categoria'),
    path('ubicaciones/<int:ubicacion_id>/eliminar/', eliminar_ubicacion, name='eliminar_ubicacion'),

    #Urls para actualizar
    path('eventos/<int:evento_id>/actualizar/', actualizar_evento, name='actualizar_evento'),
    
    #Urls de login y logout
    path('login/',login_view,name="login"),
    path('logout/',logout,name="logout"),
]
