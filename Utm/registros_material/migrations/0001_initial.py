# Generated by Django 3.2.4 on 2021-09-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(default='', max_length=20, verbose_name='Matricula')),
                ('nombre_alumno', models.CharField(default='', max_length=20, verbose_name='Nombre del alumno')),
                ('carrera', models.CharField(default='', max_length=20, verbose_name='Carrera')),
                ('material', models.TextField(default='', verbose_name='Materiales')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
                'ordering': ['created'],
            },
        ),
    ]
