# Generated by Django 3.1 on 2021-07-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreE', models.CharField(max_length=200)),
                ('imagenEF', models.ImageField(upload_to='img/enfermedades')),
                ('descripcionE', models.TextField(max_length=200)),
                ('estrategia', models.TextField()),
                ('imagenET', models.ImageField(upload_to='img/enfermedades')),
            ],
        ),
    ]