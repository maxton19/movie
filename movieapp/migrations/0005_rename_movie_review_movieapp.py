# Generated by Django 4.0 on 2023-08-16 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie',
            new_name='movieapp',
        ),
    ]
