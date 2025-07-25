from django.urls import path

from .views import hello_api, reverse_view


urlpatterns = [
    path('api/hello/', hello_api),
    path("reverse/", reverse_view)
]
