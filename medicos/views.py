from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Olá, bem-vindo ao cadastro de médicos.")
