# Generated by Django 3.1.2 on 2020-10-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=30, unique=True, verbose_name='별명'),
        ),
    ]
