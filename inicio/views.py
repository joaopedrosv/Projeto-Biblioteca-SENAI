from django.shortcuts import render

from django.shortcuts import render

#Função para abrir a pagina "inicio.html" se for necessaria
def inicio(request):
    return render(request, 'inicio.html', {})
