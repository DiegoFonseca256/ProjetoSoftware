# Generated by Django 3.2.13 on 2023-09-06 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreinoCostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('area_do_treino', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=500)),
                ('duracao', models.CharField(choices=[('R', 'Rapido'), ('M', 'Mediano'), ('D', 'Demorado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TreinoPeito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('area_do_treino', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=500)),
                ('duracao', models.CharField(choices=[('R', 'Rapido'), ('M', 'Mediano'), ('D', 'Demorado')], max_length=1)),
            ],
        ),
    ]
