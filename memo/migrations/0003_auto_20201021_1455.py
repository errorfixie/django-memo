# Generated by Django 3.1.2 on 2020-10-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_usermemo_usernum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='title',
            field=models.CharField(blank=True, max_length=254, verbose_name='메모제목'),
        ),
    ]