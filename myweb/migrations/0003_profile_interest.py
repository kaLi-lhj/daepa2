# Generated by Django 2.2.4 on 2019-08-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_auto_20190727_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.TextField(blank=True, default='nothing'),
        ),
    ]
