from django.shortcuts import render, get_object_or_404, redirect
from GestorEventosApp.forms import EventoForm, LoginForm
from .models import Evento, Ubicacion,Categoria, Usuario
from .forms import CategoriaForm, LoginForm, UbicacionForm

#INICIO DE L APP

def inicio(request):
    return render(request, 'crud/inicio.html')

#LISTAS 
def lista_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'crud/lista_ubicaciones.html', {'ubicaciones': ubicaciones})

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'crud/lista_eventos.html', {'eventos': eventos})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'crud/lista_categorias.html', {'categorias': categorias})

#CREACION
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'crud/crear_evento.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')  # Reemplaza con el nombre correcto de tu URL
    else:
        form = CategoriaForm()
    return render(request, 'crud/crear_categoria.html', {'form': form})  # Ajusta la ruta del template

def crear_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ubicaciones')
    else:
        form = UbicacionForm()
    return render(request, 'crud/crear_ubicacion.html', {'form': form})

#ACTUALIZAR 
def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'crud/actualizar_evento.html', {'form': form, 'evento': evento})

#ELIMINAR

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    evento.delete()
    return redirect('lista_eventos')

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    categoria.delete()
    return redirect('lista_categorias')

def eliminar_ubicacion(request, ubicacion_id):
    ubicacion = get_object_or_404(Ubicacion, pk=ubicacion_id)
    ubicacion.delete()
    return redirect('lista_ubicaciones')

#LOGIN Y LOGOUT
def login_view(request):
    form = LoginForm(request.POST)
    if request.method =="POST" and form.is_valid(): 
        txt_usuario = form.cleaned_data.get("txt_username")
        txt_password = form.cleaned_data.get("txt_password")
        try:
            user = Usuario.objects.get(username = txt_usuario)
            #En caso de que la contraseña ingresada sea igual a la contraseña almacenada
            if user.password == txt_password:
                request.session['autenticado'] = True 
                request.session['usuario'] = user.username 
                request.session['nombre_completo'] = user.nombres +" "+ user.apellidos
                #Redireccionamos a lista de gestiones
                return redirect("lista_eventos")
            else:
                form.add_error(None, 'Contraseña incorrecta')
        except Usuario.DoesNotExist:
            form.add_error(None, 'Usuario no existe')
    return render(request,"crud/login.html",{"form" : form })


def logout(request):
    request.session.pop('autenticado',None)
    return redirect('/login')
