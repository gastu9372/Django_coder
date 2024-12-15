from app_coder.views import *
from django.urls import path
# Es buena practica escribir todas las funciones 1x1, buena practica lo explicito
urlpatterns = [
    path('inicio/', index, name="Inicio"),
    path('vtubers/', vtubers, name ="Vtubers"),
    path('mods/', mods, name="Mods"),
    path('users/', users, name="Users"),
    path('posts/', posts, name="Posts"),
    path('formulario/', formulario_vtuber_api, name="Formulario"),
    path('del_vtuber/<int:id>', eliminar_vtuber, name="Eliminar"),
    path('edit_vtuber/<int:id>', editar_vtuber, name="Editar"),
    path("login/", login_view, name = "Login" ),
]
