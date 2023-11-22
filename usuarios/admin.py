from usuarios.models import Usuario
from django.contrib import admin

#Utilizado para que o usuario admin não consiga alterar dados das pessoas, apenas visualizar
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo')
    list_editable = ('email',)
    readonly_fields = ('senha',)
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)


