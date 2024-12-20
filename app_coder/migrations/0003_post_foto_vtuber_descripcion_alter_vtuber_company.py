# Generated by Django 5.1.3 on 2024-12-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0002_user_rename_profesores_moderator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='vtuber',
            name='descripcion',
            field=models.CharField(default='Sin descrpcion', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vtuber',
            name='company',
            field=models.CharField(max_length=30),
        ),
    ]
