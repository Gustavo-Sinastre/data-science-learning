from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/cadastrar', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('disciplinas/cadastrar', views.cadastrar_disciplinas, name='cadastrar_disciplina'),
]