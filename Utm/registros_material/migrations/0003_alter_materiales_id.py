# Generated by Django 3.2.4 on 2021-09-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros_material', '0002_alter_materiales_nombre_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiales',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
