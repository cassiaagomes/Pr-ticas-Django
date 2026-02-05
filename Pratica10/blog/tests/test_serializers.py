from django.test import TestCase
from blog.models import Autor
from blog.serializers import AutorSerializer

class AutorSerializerTest(TestCase):
    def test_serializer_cria_autor(self):
        serializer = AutorSerializer(data={"nome": "Clarice Lispector"})
        self.assertTrue(serializer.is_valid(), serializer.errors)

        autor = serializer.save()
        self.assertIsInstance(autor, Autor)
        self.assertEqual(autor.nome, "Clarice Lispector")
