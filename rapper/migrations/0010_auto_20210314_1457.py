# Generated by Django 3.1.7 on 2021-03-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapper', '0009_article_created_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
