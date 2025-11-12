from django.shortcuts import render
from datetime import datetime

def home(request):
    contexto = {
        'nome': 'Cássia',
        'numero': 5,
        'now': datetime.now(),
        'is_logged_in': True,
        'idade': 20,
        'role': 'admin',
        'produtos': [
            {'nome': 'Mouse', 'preco': 50},
            {'nome': 'Teclado', 'preco': 120},
            {'nome': 'Monitor', 'preco': 900},
        ]
    }
    return render(request, 'home.html', contexto)

def contato(request, telefone):
    return render(request, 'contato.html', {'telefone': telefone})

def about(request):
    return render(request, 'about.html')
