# Generated by Django 3.1.7 on 2021-03-13 22:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapper', '0006_auto_20210313_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapper',
            name='about_him',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
