from usuarios.models import Usuario
from django import forms
from django.db.models import fields
from .models import Livros, Categoria
from django.db import models    
from datetime import date

#
class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
#Utilizado o *args, **kwargs pois não é um número de argumentos especifico, super() retorna uma instância de uma superclasse que rastreia a posição atual
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

#Forms para cadastrar a categoria do livro, ma classe de categoria onde o init faz o start da função e o super() faz uma segunda inicalização dos codigos
class CategoriaLivro(forms.Form):
    nome = forms.CharField(max_length=30)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        
        


