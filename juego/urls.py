from django.urls import path
from juego.views import juego, ganar, derrota


urlpatterns = [
    path('juego/', juego, name='proyecto'),
    path('ganar/', ganar, name='ganar'),
    path('perder/', derrota, name='derrota'),
]

