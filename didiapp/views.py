from django.shortcuts import render,redirect
from .models import TreinoCostas,TreinoPeito,treinos
# Create your views here.
def fundacao(request):
  treino_de_peito = TreinoPeito.objects.all()
  treino_de_costas = TreinoCostas.objects.all()
  treino = treinos.objects.all()
  return render(request,'academia.html', context={ "TreinodeCostas":treino_de_costas,"TreinodePeitos":treino_de_peito,"treino":treino})

def exercicio(request):
  if request.method =="POST":
    TreinoCostas.objects.create(
      titulo=request.POST["titulo"],
      area_do_treino=request.POST["area_do_treino"],
      descricao=request.POST["descricao"],
      duracao=request.POST["duracao"],
    )
    return redirect("home")
  return render(request,"forms.html", context={"type":"Adcionar"})

def update_exercicio(request,id):
  treino_costas=TreinoCostas.objects.get(id=id)
  if request.method =="POST":
    treino_costas.titulo=request.POST["titulo"]
    treino_costas.area_do_treino=request.POST["area_do_treino"]
    treino_costas.descricao=request.POST["descricao"]
    treino_costas.duracao=request.POST["duracao"]
    treino_costas.save()
    
    return redirect("home")
  return render(request,"forms.html", context={"type":"Atualizar","treino_costas":treino_costas})

def delete_exercicio(request,id):
  treino_costas=TreinoCostas.objects.get(id=id)
  if request.method =="POST":
    if "s" in request.POST:
      treino_costas.delete()
    
    return redirect("home")
  return render(request,"are_you_sure.html", context={"treino_costas": treino_costas})