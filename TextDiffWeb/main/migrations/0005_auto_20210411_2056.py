# Generated by Django 3.1.7 on 2021-04-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210328_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]
