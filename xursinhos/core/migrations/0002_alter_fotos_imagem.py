# Generated by Django 4.0.3 on 2022-04-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='imagem',
            field=models.ImageField(upload_to='fotos'),
        ),
    ]
