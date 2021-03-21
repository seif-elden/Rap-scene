# Generated by Django 3.1.5 on 2021-03-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='')),
                ('facebook', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('instgram', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
            ],
        ),
    ]
