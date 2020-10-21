# Generated by Django 3.1.2 on 2020-10-17 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermemo',
            name='userNUM',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='사용자번호'),
            preserve_default=False,
        ),
    ]
