from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieDataSerializer

# Create your views here.

class MovieDataView(viewsets.ModelViewSet):
    """ View for MovieData """
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer