from django.core.management.base import BaseCommand
from blog.models import Autor, Editora, Livro, Publica
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Gera 100 livros fictícios'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        for _ in range(100):
            autor, _ = Autor.objects.get_or_create(
                nome=fake.name()
            )

            editora, _ = Editora.objects.get_or_create(
                nome=fake.company()
            )

            livro = Livro.objects.create(
                titulo=fake.sentence(nb_words=4),
                autor=autor,
                editora=editora
            )

            Publica.objects.create(
                livro=livro,
                data_publicacao=fake.date_between(start_date='-10y', end_date='today')
            )

        self.stdout.write(
            self.style.SUCCESS('✔ 100 livros gerados com sucesso!')
        )
