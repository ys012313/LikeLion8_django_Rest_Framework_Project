# Generated by Django 3.0.8 on 2020-07-18 15:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mystorage', '0002_album_fiels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fiels',
            new_name='Files',
        ),
    ]
