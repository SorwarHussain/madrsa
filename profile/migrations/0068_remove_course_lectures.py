# Generated by Django 4.1.7 on 2023-02-25 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0067_alter_video_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lectures',
        ),
    ]
