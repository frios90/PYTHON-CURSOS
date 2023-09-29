from django.urls import path
from . import views

urlpatterns = [


    path('index/', views.index),
    


    path('', views.hello),
    path("otra/", views.otraFuncion),
    path("parametros/<str:username>", views.parametros),
    path("projects/", views.projects),
    path("project/<int:id>", views.project)

]