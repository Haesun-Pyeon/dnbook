# Generated by Django 2.2.3 on 2019-11-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0024_auto_20191119_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='store/', verbose_name='외관사진 등록'),
        ),
    ]
