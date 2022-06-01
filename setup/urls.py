from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecoViewSet


router = routers.DefaultRouter()
router.register('pontosturisticos', PontoTuristicoViewSet)
router.register('atracoes', AtracoesViewSet)
router.register('enderecos', EnderecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
