
from django import forms
from .models import Evento, Ubicacion, Categoria

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'categoria']

    ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), empty_label="Selecciona una ubicación")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecciona una categoría")
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class LoginForm(forms.Form):
    txt_username  = forms.CharField()
    txt_password =forms.CharField(widget = forms.PasswordInput)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        
class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'region']