# Generated by Django 3.1.7 on 2021-03-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('bodypart', models.CharField(choices=[('LE', 'legs'), ('AR', 'arms'), ('BA', 'back'), ('CH', 'chest'), ('SH', 'shoulders'), ('CO', 'core'), ('OT', 'other')], max_length=2)),
            ],
        ),
    ]
