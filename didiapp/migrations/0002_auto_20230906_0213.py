# Generated by Django 3.2.13 on 2023-09-06 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treinocostas',
            name='descricao',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='treinopeito',
            name='area_do_treino',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='treinopeito',
            name='descricao',
            field=models.CharField(max_length=5000),
        ),
    ]
