from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.models import Avatar



def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "app_music/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})




def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"app_music/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':

        Formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if Formulario.is_valid():
            if Formulario.cleaned_data.get("imagen"):
                avatar = Avatar(user=usuario, imagen=Formulario.cleaned_data.get("imagen"))
                #usuario.avatar.imagen = Formulario.cleaned_data.get("imagen")
                avatar.save()
            Formulario.save()
            return render(request, "app_music/index.html")

    else:
        Formulario = UserEditForm(instance=usuario)

    return render(request,"users/editar_usuario.html",{"form": Formulario,"usuario": usuario})

class CambiarClaveView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_clave.html"
    success_url = reverse_lazy("EditarUsuario")