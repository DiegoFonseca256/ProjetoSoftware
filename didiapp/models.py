from django.db import models

class TreinoPeito(models.Model):
  DEMORA= [
    ("R",'Rapido'),
    ("M",'Mediano'),
    ("D",'Demorado')
  ]
  titulo = models.CharField(max_length=50)
  area_do_treino = models.CharField(max_length=20)
  descricao = models.CharField(max_length=5000)
  duracao = models.CharField(max_length=40)

class TreinoCostas(models.Model):
  DEMORA = [
    ("R",'Rapido'),
    ("M",'Mediano'),
    ("D",'Demorado')
  ]
  titulo = models.CharField(max_length=50)
  area_do_treino = models.CharField(max_length=20)
  descricao = models.CharField(max_length=5000)
  duracao = models.CharField(max_length=1, choices=DEMORA)

class treinos(models.Model):
  ESCALA = [
    ("C",'Chato'),
    ("L",'Legal'),
    ("M",'Muito Legal')
  ]
  DOR = [
    ("N",'Nao Doi'),
    ("D",'Doi'),
    ("M",'Doi Muito')
  ]
  QNT = [
    ("1",'1'),
    ("2",'2'),
    ("3",'3'),
    ("4",'4'),
    ("5",'5'),
    ("6",'6'),
  ]
  titulo = models.CharField(max_length=50)
  escala_satifacao = models.CharField(max_length=1, choices=ESCALA)
  dor = models.CharField(max_length=1, choices=DOR)
  quantidade_semanal_de_exer = models.CharField(max_length=1, choices=QNT)