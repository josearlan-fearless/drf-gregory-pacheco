from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, )
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    filter_fields = ('nome', 'descricao', 'endereco')
    search_fields = ['nome', 'descricao', 'endereco__linha1']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpResponse('Okay!')
