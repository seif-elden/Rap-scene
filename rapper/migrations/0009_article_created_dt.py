# Generated by Django 3.1.7 on 2021-03-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapper', '0008_auto_20210314_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
