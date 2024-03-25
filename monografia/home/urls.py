from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


from .views import monografiaCreate
from .views import monografiaUpdate
from .views import monografiaDelete




app_name = "home"

urlpatterns = [
    path("", views.monografiaList.as_view(), name="list"),
    #path("home/", views.monografiaList.as_view(), name="list1"),
    path("home/cadastro", login_required(monografiaCreate.as_view()), name="cadastro"),
    path("home/editar/<int:pk>", login_required(monografiaUpdate.as_view()), name="editar"),
    path("home/excluir/<int:pk>", login_required(monografiaDelete.as_view()), name="excluir"),    
    ]
