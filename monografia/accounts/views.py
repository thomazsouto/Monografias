import imp
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


class UsuarioCreate(GroupRequiredMixin,generic.CreateView):
    template_name = 'registration/register.html'
    form_class = UsuarioForm
    group_required = u'Admin'
    success_url = reverse_lazy('login')

 
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Usuario")       
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        #print(type(self.object),self.object,dir(self.object))
        send_mail("Confirmação de cadastro", "Sua conta foi criada com sucesso",'sistema@monografia.com.br',[self.object.email])
        return url

    