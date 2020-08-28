from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()
    
    if perfil_id == 1:
        perfil = Perfil(1, 'Elvis','elvis@gmail.com', '99999-9999', 'IFPI')

    if perfil_id == 2:
        perfil = Perfil(2, 'Lucas', 'lucas@gmail.com', '98888-8888', 'UFPI')

    return render(request, 'perfil.html', { "perfil" : perfil})