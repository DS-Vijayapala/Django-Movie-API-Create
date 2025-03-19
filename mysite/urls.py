"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from Movies.views import MovieDataView, ActionMovieDataView , cartoonMovieDataView

router = routers.SimpleRouter()
router.register('movies', MovieDataView , basename='movie')
router.register('action', ActionMovieDataView , basename='action')
router.register('cartoon', cartoonMovieDataView , basename='cartoon')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
