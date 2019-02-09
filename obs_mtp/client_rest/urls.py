from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_dados/', views.buscar_dados,  name='buscar_dados'),
]