from django.urls import path
from .views import lista_livros

urlpatterns = [
    path('', lista_livros, name='lista_livros'),
]
