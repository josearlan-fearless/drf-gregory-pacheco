from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet


router = routers.DefaultRouter()
router.register('pontosturisticos', PontoTuristicoViewSet)
router.register('atracoes', AtracaoViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
