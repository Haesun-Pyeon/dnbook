
# Generated by Django 2.2.3 on 2019-10-17 07:05


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0014_stamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookstore',
            name='like_count',
        ),
    ]
