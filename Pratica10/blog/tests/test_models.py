from django.test import TestCase
from blog.models import Autor

class AutorModelTest(TestCase):
    def test_str_retorna_nome(self):
        autor = Autor.objects.create(nome="Machado de Assis")
        self.assertEqual(str(autor), "Machado de Assis")
