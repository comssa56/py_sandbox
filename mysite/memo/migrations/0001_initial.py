# Generated by Django 4.0.3 on 2022-04-04 13:07

import datetime
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_text', models.CharField(max_length=200)),
                ('insert_date', models.DateTimeField(default=datetime.datetime(2022, 4, 4, 22, 7, 33, 125058), verbose_name='date inserted')),
            ],
            options={
                'db_table': 'tbl_memo_memo',
            },
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips_text', models.CharField(max_length=200)),
                ('insert_date', models.DateTimeField(default=datetime.datetime(2022, 4, 4, 22, 7, 33, 125058), verbose_name='date inserted')),
                ('memo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memo.memo')),
            ],
            options={
                'db_table': 'tbl_memo_tips',
            },
        ),
    ]