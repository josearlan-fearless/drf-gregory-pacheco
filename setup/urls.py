from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet


router = routers.DefaultRouter()
router.register('pontosturisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register('atracoes', AtracaoViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('comentarios', ComentarioViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
