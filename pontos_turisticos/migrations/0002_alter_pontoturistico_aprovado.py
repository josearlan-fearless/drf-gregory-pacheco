# Generated by Django 3.2.13 on 2022-05-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
