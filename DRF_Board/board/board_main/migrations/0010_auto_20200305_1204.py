# Generated by Django 2.1.2 on 2020-03-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_main', '0009_auto_20200303_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='date',
            field=models.DateField(auto_now_add=True, db_column='DATE', null=True),
        ),
    ]
