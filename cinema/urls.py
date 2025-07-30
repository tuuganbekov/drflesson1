from django.urls import path

from .views import hello_api, reverse_view, reverse_number, movies_list, genre_list


urlpatterns = [
    path('cinema/hello/', hello_api),
    path("cinema/reverse/", reverse_view),
    path("cinema/reverse-number/", reverse_number),
    path('cinema/movies/', movies_list),
    path('cinema/genres/', genre_list),

]
