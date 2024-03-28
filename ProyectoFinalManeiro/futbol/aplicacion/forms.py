from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RepresentanteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    agencia = forms.CharField(label="Agencia de Representacion", max_length=50, required=True)
    email = forms.EmailField(required=True) 


class FutbolistaForm(forms.Form):
    nombreCompleto = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=50, required=True)
    dorsal = forms.IntegerField(label="Dorsal", required=True)
    equipo = forms.CharField(label="Equipo", max_length=50, required=True)

class EntrenadorForm(forms.Form):
    nombreCompleto = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=50, required=True)
    equipo = forms.CharField(label="Equipo", max_length=50, required=True)


class EquipoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    pais = forms.CharField(label="Pais", max_length=50, required=True)
    nroSocios = forms.IntegerField(label="Cantidad de Socios", required=True)
    fechaFundacion = forms.DateField(label="Fecha de Fundacion", required=True)

class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)