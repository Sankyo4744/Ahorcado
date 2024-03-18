from django.urls import path
from juego.views import juego


urlpatterns = [
    path('juego/', juego)
]
