# Generated by Django 4.2.2 on 2023-07-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_description',
            field=models.TextField(default='Описание отсутствует', verbose_name='Описание'),
        ),
    ]
