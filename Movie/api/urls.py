from django.urls import path
from . import viewsets

urlpatterns = [
    path('', viewsets.MovieRest.as_view() , name = 'movie_rest'),
    path('/<int:pk>', viewsets.MovieRest.as_view() , name = 'movie_rest'),
]
