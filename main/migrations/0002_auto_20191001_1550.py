# Generated by Django 2.2.5 on 2019-10-01 06:50

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bossprofile',
            managers=[
                ('object', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='normalprofile',
            managers=[
                ('object', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
