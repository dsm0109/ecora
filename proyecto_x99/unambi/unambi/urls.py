"""unambi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from unambi.apps.usuario import views as views_usuario


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views_usuario.LoginView, name="Login"),
    url(r'^registrar/$', views_usuario.RegisterView, name="Registro"),
    url(r'^inicio/$', views_usuario.InicioView, name="Inicio"),
    url(r'^mi-perfil/$', views_usuario.MiPerfilView, name="Mi perfil"),
    url(r'^amigos/$', views_usuario.AmigosView, name="Amigos"),
    url(r'^insignias/$', views_usuario.InsigniaView, name="Insignia"),
    url(r'^mapa/$', views_usuario.MapaView, name="Mapa"),
    url(r'^eventos/$', views_usuario.EventoView, name="Evento"),
    url(r'^configuracion/$', views_usuario.ConfiguracionView, name="Configuracion"),
    url(r'^preguntas/$', views_usuario.PreguntasView, name="Preguntas"),
    url(r'^logOut/$', views_usuario.LogOut, name="Log Out"),

]
