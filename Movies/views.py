from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieDataSerializer

# Create your views here.


class MovieDataView(viewsets.ModelViewSet):
    """ View for MovieData """
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer


class ActionMovieDataView(viewsets.ModelViewSet):
    """ View for Action MovieData """
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieDataSerializer


class cartoonMovieDataView(viewsets.ModelViewSet):
    """ View for cartoon MovieData """
    queryset = MovieData.objects.filter(typ='cartoon')
    serializer_class = MovieDataSerializer
