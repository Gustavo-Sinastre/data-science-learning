from django.shortcuts import render, redirect
from .models import Aluno
from .models import Disciplina
from .forms import AlunoForm
from .forms import DisciplinaForm

# Listar alunos
def listar_alunos(request):
    alunos = Aluno.objects.all()
    contexto = {"alunos": alunos}
    return render(request, "listar_alunos.html", contexto)

def cadastrar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, "cadastrar_aluno.html", {"form": form})
    
def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    contexto = {"disciplinas": disciplinas}
    return render(request, "listar_disciplinas.html", contexto)

def cadastrar_disciplinas(request):
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm()  # O formulário é criado aqui, no else
    return render(request, "cadastrar_disciplina.html", {"form": form})

