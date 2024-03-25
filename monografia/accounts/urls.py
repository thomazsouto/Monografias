from django import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
   path('register/', login_required(views.UsuarioCreate.as_view()), name='registrar'),
] 