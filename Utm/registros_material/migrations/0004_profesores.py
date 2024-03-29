# Generated by Django 3.2.4 on 2021-09-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros_material', '0003_alter_materiales_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=60, verbose_name='Nombre del Encargado')),
                ('Grado', models.CharField(default='', max_length=60, verbose_name='Grado de estudio del encargado')),
                ('Matricula', models.IntegerField(verbose_name='Matricula del encargado')),
                ('Laboratorio', models.CharField(default='', max_length=60, verbose_name='Nombre del area del laboratorio')),
                ('Numero', models.IntegerField(verbose_name='Numero del laboratorio')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='imagen del encargado')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'ordering': ['created'],
            },
        ),
    ]
