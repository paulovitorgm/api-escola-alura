# Generated by Django 4.2 on 2023-05-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alunos',
            new_name='Aluno',
        ),
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
    ]
