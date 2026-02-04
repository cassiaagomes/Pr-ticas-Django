from django.shortcuts import render, redirect
from .forms import LivroForm

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_livro')
    else:
        form = LivroForm()

    return render(request, 'biblioteca/cadastrar_livro.html', {'form': form})
