# Generated by Django 2.2.6 on 2019-10-28 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191028_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bossprofile',
            name='level',
        ),
    ]