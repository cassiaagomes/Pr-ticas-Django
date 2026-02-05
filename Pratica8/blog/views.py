from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

from .models import Livro


def listar_livros(request):
    livros = Livro.objects.select_related('autor', 'editora').all()
    paginator = Paginator(livros, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/listar_livros.html', {'page_obj': page_obj})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lista_livros")  # nome da rota
    else:
        form = UserCreationForm()

    return render(request, "auth/signup.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "auth/login.html"


class CustomLogoutView(LogoutView):
    pass


@login_required
def criar_livro(request):
    return render(request, "blog/criar_livro.html")


@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, "blog/editar_livro.html", {"livro": livro})
