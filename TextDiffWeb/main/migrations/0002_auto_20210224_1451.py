# Generated by Django 3.1.7 on 2021-02-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='texts',
            options={'verbose_name': 'Текст', 'verbose_name_plural': 'Тексты'},
        ),
        migrations.AddField(
            model_name='texts',
            name='url',
            field=models.CharField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='score',
            field=models.IntegerField(blank=True, verbose_name='Оценка сложности'),
        ),
    ]
