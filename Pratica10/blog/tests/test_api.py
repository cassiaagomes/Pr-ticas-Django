from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from blog.models import Autor

class AutorApiTest(APITestCase):
    def test_crud_basico_autor(self):
        url_list = reverse("autor-list")

        resp_post = self.client.post(url_list, {"nome": "José Saramago"}, format="json")
        self.assertEqual(resp_post.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Autor.objects.filter(nome="José Saramago").exists())

        resp_get = self.client.get(url_list)
        self.assertEqual(resp_get.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp_get.data), 1)
