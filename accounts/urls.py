from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('registro/', views.registro_request, name='registro'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('avatar/subir/', views.agregar_avatar, name='agregar_avatar'),
]