# Generated by Django 3.1.7 on 2021-03-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='language_of_publication',
            field=models.CharField(choices=[('TR', 'Türkçe'), ('EN', 'İngilizce'), ('FR', 'Fransızca'), ('DE', 'Almanca'), ('RU', 'Rusça'), ('IT', 'İtalyanca')], default='EN', max_length=3),
        ),
        migrations.AlterField(
            model_name='bookdetail',
            name='skin_condition',
            field=models.CharField(choices=[('H', 'Ciltli'), ('U', 'Ciltsiz')], default='H', max_length=3),
        ),
    ]
