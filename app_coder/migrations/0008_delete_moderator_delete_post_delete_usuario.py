# Generated by Django 5.1.3 on 2024-12-23 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0007_profile_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Moderator',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
