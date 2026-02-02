from django.urls import path
from . import views


app_name='recette'

urlpatterns=[
    path('affiche', views.index, name='index'),
    path('details/<str:immatriculation>/',views.details,name='details')

]