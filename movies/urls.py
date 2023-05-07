from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("movies", views.movies,name="movies"),
    path("movies/<slug:slug>",views.movie_details,name="movie-details")
]
