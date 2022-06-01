from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet


router = routers.DefaultRouter()
router.register('pontosturisticos', PontoTuristicoViewSet)
router.register('atracoes', AtracoesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
