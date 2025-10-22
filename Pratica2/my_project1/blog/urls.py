from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('eco/<str:texto>/', views.eco),
    path('info/', views.info),
]
