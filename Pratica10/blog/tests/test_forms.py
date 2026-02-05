from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm

class SignupFormTest(TestCase):
    def test_usercreationform_senhas_diferentes_invalida(self):
        form = UserCreationForm(data={
            "username": "cassia",
            "password1": "SenhaForte123!",
            "password2": "SenhaDiferente123!",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)
