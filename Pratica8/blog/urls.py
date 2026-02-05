from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='lista_livros'),
    path('novo/', views.criar_livro, name='criar_livro'),
    path('editar/<int:id>/', views.editar_livro, name='editar_livro'),
]
