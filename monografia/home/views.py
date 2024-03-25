from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin

from .models import monografia
from .serializers import monografiaSerializer


class monografiaList(ListView):
    model = monografia
    template_name = 'monografia_list.html'


#class monografiaDetailView(DetailView):
#    model = monografia

#criar formulario
class monografiaCreate(GroupRequiredMixin,CreateView):
    model = monografia
    group_required = u"Admin","Usuario"
    fields = ['titulo', 'autor', 'ano', 'orientador', 'resumo', 'link']
    template_name = 'home/form.html'
    success_url = '/'


class monografiaUpdate(UpdateView):
    model = monografia
    group_required = u"Admin","Usuario"
    fields = ['titulo', 'autor', 'ano', 'orientador', 'resumo', 'link']
    template_name = 'home/form-edit.html'
    success_url = '/'


#Excluir formulario

class monografiaDelete(DeleteView):
    model = monografia
    group_required = u"Admin","Usuario"
    template_name = 'home/form-del.html'
    success_url = '/'

# API Rest

class monografiaViewSet(viewsets.ModelViewSet):
    queryset = monografia.objects.all()
    serializer_class = monografiaSerializer