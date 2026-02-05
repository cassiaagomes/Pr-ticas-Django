from django.test import TestCase
from django.urls import reverse
from blog.models import Autor, Editora, Livro

class ListarLivrosViewTest(TestCase):
    def test_listar_livros_paginado_10_por_pagina(self):
        autor = Autor.objects.create(nome="Autor 1")
        editora = Editora.objects.create(nome="Editora 1")

        # cria 12 livros
        for i in range(12):
            Livro.objects.create(titulo=f"Livro {i}", autor=autor, editora=editora)

        url = reverse("lista_livros")  # precisa bater com seu name na urls.py
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("page_obj", resp.context)
        self.assertEqual(len(resp.context["page_obj"].object_list), 10)
