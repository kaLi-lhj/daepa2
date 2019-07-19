# Generated by Django 2.2.3 on 2019-07-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('context', models.TextField(default='')),
                ('view_cnt', models.IntegerField(default=0)),
                ('like_cnt', models.IntegerField(default=0)),
                ('hate_cnt', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('no_del', models.BooleanField(default=False)),
            ],
        ),
    ]
