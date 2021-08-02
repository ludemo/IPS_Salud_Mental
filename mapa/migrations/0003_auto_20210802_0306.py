# Generated by Django 3.1 on 2021-08-02 03:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0002_auto_20210728_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(15)]),
        ),
    ]