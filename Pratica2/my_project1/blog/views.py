from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, texto):
    return HttpResponse(f"Você digitou: {texto}")

def info(request):
    data = {
        "disciplina": "RAD",
        "framework": "Django",
        "semestre": "2025.2"
    }
    return JsonResponse(data)
