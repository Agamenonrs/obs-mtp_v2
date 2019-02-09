from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_dados/', views.buscar_dados,  name='buscar_dados'),
    path('form_iniciar/', views.form_iniciar,  name='form_iniciar'),
    path('exibe_ultimo_registro/', views.exibe_ultimo_registro,  name='exibe_ultimo_registro'),
]