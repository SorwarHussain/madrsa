# Generated by Django 4.0.3 on 2022-06-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0023_alter_profile_ereasonmarry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='eeducation',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ejob',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ejobcontinue',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ereasonMarry',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ewifeDowry',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ewifeeducation',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ewifejob',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ewifeporda',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ewifestay',
            field=models.CharField(blank=True, max_length=354, null=True),
        ),
    ]