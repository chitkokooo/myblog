# Generated by Django 3.0.7 on 2020-08-24 06:06

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blogs.models.Blog.image_path),
        ),
    ]
