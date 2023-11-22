from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


#Função de logar
def login(request):
    if request.session.get('usuario'):
        return redirect('/livro/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

#Função de efetuar cadastro
def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/livro/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

#Função para verificar o cadastro e validar se for valido
def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadatro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          senha = senha,
                          email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

#Função de validar o login caso a sessão seja valida
def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/livro/home/')

    return HttpResponse(f"{email} {senha}")

#Função de sair da sessão
def sair(request):
    request.session.flush()
    return redirect('/auth/login/')