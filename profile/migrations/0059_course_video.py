# Generated by Django 4.1.7 on 2023-02-22 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0058_course_slug_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.ManyToManyField(to='profile.video'),
        ),
    ]
