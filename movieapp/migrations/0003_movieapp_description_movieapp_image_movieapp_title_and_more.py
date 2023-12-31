# Generated by Django 4.0 on 2023-08-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_movie_movieapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieapp',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='movieapp',
            name='image',
            field=models.ImageField(blank=True, upload_to='movieapp/images/'),
        ),
        migrations.AddField(
            model_name='movieapp',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movieapp',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
