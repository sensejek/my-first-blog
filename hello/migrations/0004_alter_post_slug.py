# Generated by Django 4.0.5 on 2022-06-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]