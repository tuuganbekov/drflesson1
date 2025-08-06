from django.urls import path

from .views import (
    GenreAPIView,
    GenreRetrieveUpdateDestroyAPIView,
    MovieAPIView,
    MovieRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('cinema/genres/', GenreAPIView.as_view(), name='genres'),
    path('cinema/genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('cinema/movies/', MovieAPIView.as_view(), name='movies'),
    path('cinema/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
]