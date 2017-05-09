from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from unambi.apps.usuario.formUser import LoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/inicio')
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            Usuario = lf.cleaned_data['username']
            Pass = lf.cleaned_data['password']
            user = authenticate(username=Usuario, password=Pass)
            if user is not None:
                login(request, user)
                return redirect('/inicio')
            else:
                LoginF = LoginForm()

    else:
        LoginF = LoginForm()

    return render(request, 'login.html', {'login': LoginF})

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('/inicio')
    if request.method == 'POST':
        lf = RegisterForm(request.POST)
        if lf.is_valid():
            usuario = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            email = lf.cleaned_data['email']
            user = User.objects.create_user(usuario, email, password)
            user.save()
            userAux = authenticate(username=usuario, password=password)
            login(request, userAux)
            return redirect('/inicio')

        else:
            LoginF = LoginForm()

    else:
        LoginF = RegisterForm()
    return render(request, 'register.html', {'register': LoginF})

def InicioView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'inicio.html',{})

def MiPerfilView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'mi-perfil.html',{})


def AmigosView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'amigos.html',{})

def InsigniaView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'insignias.html', {})


def MapaView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'mapa.html',{})

def ConfiguracionView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'configuracion.html',{})

def PreguntasView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'preguntas.html',{})

def EventoView(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'eventos.html',{})

def LogOut(request):
    logout(request)
    return redirect('/')