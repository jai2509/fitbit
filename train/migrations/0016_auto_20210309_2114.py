# Generated by Django 3.1.7 on 2021-03-09 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0015_auto_20210309_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='time',
            field=models.CharField(max_length=15),
        ),
    ]