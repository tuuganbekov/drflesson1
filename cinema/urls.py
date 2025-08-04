from django.urls import path

from .views import (
    hello_api,
    reverse_view, 
    reverse_number, 
    movies_list, 
    genre_list,
    genre_detail,
    genre_update,
    genre_delete,
    user_register
)


urlpatterns = [
    path('cinema/hello/', hello_api),
    path("cinema/reverse/", reverse_view),
    path("cinema/reverse-number/", reverse_number),
    path('cinema/movies/', movies_list),
    path('cinema/genres/', genre_list),
    path('cinema/genres/<int:pk>/', genre_detail),
    path('cinema/genres/update/<int:pk>/', genre_update),
    path('cinema/genres/delete/<int:pk>/', genre_delete),
    path('cinema/registration/', user_register)
]
