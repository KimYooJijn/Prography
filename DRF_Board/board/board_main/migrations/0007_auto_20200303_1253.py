# Generated by Django 2.1.2 on 2020-03-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_main', '0006_auto_20200303_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='date',
            field=models.DateField(auto_now=True, db_column='DATE', null=True),
        ),
    ]
