from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perros/', views.perros, name='perros'), 
    path('gatos/', views.gatos, name='gatos'),
    path('comidaperros/', views.comidaperros, name='comidaperros'), 
    path('comidagatos/', views.comidagatos, name='comidagatos'),
    path('registro/', views.registro, name='registro'),
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('usuarios/nuevo/', views.usuario_nuevo, name='usuario_nuevo'),
    path('usuarios/<int:pk>/editar/', views.usuario_editar, name='usuario_editar'),
    path('usuarios/<int:pk>/eliminar/', views.usuario_eliminar, name='usuario_eliminar'),
    path('registro/', views.registrar_usuario, name='registro'),
    # Agrega otras rutas aquí
]