# Generated by Django 2.2.6 on 2019-11-26 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0029_merge_20191126_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='addr',
            field=models.TextField(unique=True, verbose_name='책방주소'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='store/', verbose_name='외관사진'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='insta',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='인스타그램'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='name',
            field=models.CharField(default='storename', max_length=20, null=True, verbose_name='책방이름'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='openhour',
            field=models.TextField(blank=True, null=True, verbose_name='영업시간'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='000-0000-0000과 같은 형식으로 입력해주세요.', regex='^\\d{2,3}\\-\\d{3,4}\\-\\d{4}$')], verbose_name='전화번호'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='웹사이트'),
        ),
    ]