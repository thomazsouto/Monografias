from django.contrib import admin
from django.urls import include, path
from home.views import monografiaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'monografias', monografiaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', include('home.urls', namespace='home')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/', include(router.urls)),       
] 