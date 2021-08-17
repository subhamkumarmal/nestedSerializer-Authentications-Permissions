import django_filters
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

from .models import Singers,Writers,Songs
from .serializers import SongSeri,SingerSeri,WriterSeri
from rest_framework import generics, filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import  BasicAuthentication
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# Create your views here.
@login_required()
def ViewsList(request):
    return render(request,'nsapp/index.html')

class SongsView(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSeri


    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['lyrics']

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['lyrics']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['lyrics']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]






class SingerView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Singers.objects.all()
    serializer_class = SingerSeri


class WriterView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Writers.objects.all()
    serializer_class = WriterSeri

