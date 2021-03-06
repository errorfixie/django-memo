# Generated by Django 3.1.2 on 2020-10-21 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='메모제목')),
                ('contents', models.TextField(blank=True, verbose_name='메모내용')),
                ('memodate', models.DateTimeField(auto_now_add=True, verbose_name='메모등록날짜')),
                ('memoupdate', models.DateTimeField(auto_now=True, verbose_name='메모수정날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Usermemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memoNUM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memo.memo', verbose_name='메모번호')),
            ],
        ),
    ]
