from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_publicacao = models.DateField()
