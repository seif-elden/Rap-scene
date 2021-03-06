# Generated by Django 3.1.7 on 2021-03-14 10:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapper', '0007_auto_20210314_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='rapper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rapper.rapper', verbose_name='music'),
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_content', ckeditor.fields.RichTextField()),
                ('rapper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rapper.rapper', verbose_name='article')),
            ],
        ),
    ]
