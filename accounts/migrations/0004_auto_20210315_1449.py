# Generated by Django 3.1.7 on 2021-03-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_community_post_visable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_post',
            name='caption',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]
