# Generated by Django 2.2.6 on 2019-10-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0015_remove_bookstore_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='stamp',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
