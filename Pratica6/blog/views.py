from django.shortcuts import render

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.select_related('autor', 'editora').all()
    paginator = Paginator(livros, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/listar_livros.html', {
        'page_obj': page_obj
    })
