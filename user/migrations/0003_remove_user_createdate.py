# Generated by Django 3.1.2 on 2020-10-15 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201015_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='createdate',
        ),
    ]
