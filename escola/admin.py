from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
    list_display_links = ['id', 'nome']
    search_fields = ['nome']
    list_per_page = 10
    
# class Cursos(admin.ModelAdmin):
#     list_display = ['codigo_curso', 'descricao', 'nivel']
#     list_display_links = ['codigo_curso', 'descricao']
#     search_fields = ['codigo_curso','descricao']
#     list_per_page = 10
#     list_filter = ['nivel']

class Matriculas(admin.ModelAdmin):
    list_display = ['id','aluno', 'curso', 'turno' ]
    list_display_links = ['id', 'aluno']
    list_per_page = 10
    list_filter = ['turno']

admin.site.register(Aluno, Alunos)
admin.site.register(Curso)
admin.site.register(Matricula, Matriculas)