# Generated by Django 4.0 on 2021-12-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_data',
        ),
        migrations.AddField(
            model_name='video',
            name='video_path',
            field=models.CharField(default='', max_length=255, verbose_name='video file path'),
        ),
    ]
