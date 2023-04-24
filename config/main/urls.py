from django.urls import path
from .views import MovieCreateView, MovieUpdateView, MovieDeleteView, MovieListView


app_name = "main"
urlpatterns = [
    path("movies/all/", MovieListView.as_view(), name="movie_list"),
    path("movies/", MovieCreateView.as_view(), name="movie_create"),
    path("movies/<int:pk>/", MovieUpdateView.as_view(), name="movie_update"),
    path("movies/delete/<int:pk>/", MovieDeleteView.as_view(), name="movie_delete"),
]
