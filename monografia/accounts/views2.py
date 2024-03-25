from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from braces.views import GroupRequiredMixin

class SignUp(GroupRequiredMixin,generic.CreateView):
    form_class = UserCreationForm
    group_required = u'Admin'
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    