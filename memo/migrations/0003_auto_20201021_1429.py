# Generated by Django 3.1.2 on 2020-10-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_usermemo_usernum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='memoupdate',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='메모수정날짜'),
        ),
    ]
