from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordChangeView



# Create your views here.

#Paginas Principales
def home(request):
    return render(request, "aplicacion/home.html")
def acerca(request):
    return render(request, "aplicacion/acerca_mi.html") 
#______________________________________________________


@login_required
def futbolistas(request):
    return render(request, "aplicacion/futbolistas.html")

@login_required
def equipo(request):
    return render(request, "aplicacion/equipo.html")

@login_required
def entrenador(request):
    return render(request, "aplicacion/entrenador.html")

#Funciones para vista de Modelos
@login_required
def futbolistas(request):
    ctx = {'futbolistas': Futbolista.objects.all()}
    return render(request, "aplicacion/futbolistas.html", ctx)
@login_required
def entrenadores(request):
    ctx= {'entrenadores': Entrenador.objects.all()}
    return render (request, 'aplicacion/entrenadores.html', ctx)

#Funciones para Futbolistas
@login_required
def buscarFutbolista(request):
    return render(request, "aplicacion/buscar_futbolista.html")

@login_required
def buscar(request):
    if request.GET['buscar']:
        nombre = request.GET['buscar']
        futbolista = Futbolista.objects.filter(nombreCompleto=nombre)
        if futbolista:
            contexto = {"futbolista": futbolista, 'descripcion': 'Futbolista'}
        else:
            contexto = {
                'descripcion': f"No se encontro un futbolista con nombre: {nombre}"
            }
       
    return render(request, "aplicacion/futbolista.html", contexto)

# Vista de lista, update, create y delete de Futbolistas
class FutbolistaList(LoginRequiredMixin, ListView):
    model = Futbolista
class FutbolistaCreate(LoginRequiredMixin, CreateView):
    model = Futbolista
    fields = ['nombreCompleto', 'nacionalidad', 'equipo', 'dorsal']
    success_url = reverse_lazy('futbolistas')
class FutbolistaUpdate(LoginRequiredMixin, UpdateView):
    model = Futbolista
    fields = ['nombreCompleto', 'nacionalidad', 'equipo', 'dorsal']
    success_url = reverse_lazy('futbolistas')
class FutbolistaDelete(LoginRequiredMixin, DeleteView):
    model = Futbolista
    success_url = reverse_lazy('futbolistas')

#Vista de lista, update, create y delete de Entrenadores
class EntrenadorList(LoginRequiredMixin, ListView):
    model = Entrenador
class EntrenadorCreate(LoginRequiredMixin, CreateView):
    model = Entrenador
    fields = ['nombreCompleto', 'nacionalidad', 'equipo']
    success_url = reverse_lazy('entrenador')
class EntrenadorUpdate(LoginRequiredMixin, UpdateView):
    model = Entrenador
    fields = ['nombreCompleto', 'nacionalidad', 'equipo']
    success_url = reverse_lazy('entrenador')
class EntrenadorDelete(LoginRequiredMixin, DeleteView):
    model = Entrenador
    success_url = reverse_lazy('entrenador')


#Vista de lista, update, create y delete de Representantes
class RepresentanteList(LoginRequiredMixin, ListView):
    model = Representante
class RepresentanteCreate(LoginRequiredMixin, CreateView):
    model = Representante
    fields = ['nombre', 'apellido', 'agencia', 'email']
    success_url = reverse_lazy('representante')
class RepresentanteUpdate(LoginRequiredMixin, UpdateView):
    model = Representante
    fields = ['nombre', 'apellido', 'agencia', 'email']
    success_url = reverse_lazy('representante')
class RepresentanteDelete(LoginRequiredMixin, DeleteView):
    model = Representante
    success_url = reverse_lazy('representante')


#Vista de lista, update, create y delete de Equipos
class EquipoList(LoginRequiredMixin, ListView):
    model = Equipo
class EquipoCreate(LoginRequiredMixin, CreateView):
    model = Equipo
    fields = ['nombre', 'pais', 'nroSocios', 'fechaFundacion']
    success_url = reverse_lazy('equipo')
class EquipoUpdate(LoginRequiredMixin, UpdateView):
    model = Equipo
    fields = ['nombre', 'pais', 'nroSocios', 'fechaFundacion']
    success_url = reverse_lazy('equipo')
class EquipoDelete(LoginRequiredMixin,DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipo')


#Funciones Representantes
    
@login_required
def buscarRepresentante(request):
    return render(request, "aplicacion/buscar_representante.html")

@login_required
def buscaDeRepresentante(request):
    if request.GET['buscar']:
        apellido = request.GET['buscar']
        representante = Representante.objects.filter(apellido=apellido)
        if representante:
            contexto = {"representante": representante, 'descripcion': 'Representante'}
        else:
            contexto = {
                'descripcion': f"No se encontro el Representante: {apellido}"
            }
       
    return render(request, "aplicacion/representante.html", contexto)


#Funciones Entrenadores
@login_required
def buscarEntrenador(request):
    return render(request, "aplicacion/buscar_entrenador.html")

@login_required
def buscaDeEntrenador(request):
    if request.GET['buscar']:
        nombre = request.GET['buscar']
        entrenador = Entrenador.objects.filter(nombreCompleto=nombre)
        if entrenador:
            contexto = {"entrenador": entrenador, 'descripcion': 'Entrenador'}
        else:
            contexto = {
                'descripcion': f"No se encontro un Entrenador con nombre: {nombre}"
            }
       
    return render(request, "aplicacion/entrenador.html", contexto)

#Funciones Equipos
@login_required
def buscarEquipo(request):
    return render(request, "aplicacion/buscar_equipo.html")

@login_required
def buscaDeEquipo(request):
    if request.GET['buscar']:
        nombre = request.GET['buscar']
        equipo = Equipo.objects.filter(nombre=nombre)
        if equipo:
            contexto = {"equipo": equipo, 'descripcion': 'Equipo'}
        else:
            contexto = {
                'descripcion': f"No se encontro un Equipo con nombre: {nombre}"
            }
       
    return render(request, "aplicacion/equipo.html", contexto)

# Login, Logout, Autenticacion, Registracion y Edicion de Usuario
 
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #Carga De Avatar
            try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                    avatar = "/media/avatares/user.png"
            finally:
                    request.session["avatar"] = avatar
            #________________________________
            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} ) 

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )   

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")  


# Avatares
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )        