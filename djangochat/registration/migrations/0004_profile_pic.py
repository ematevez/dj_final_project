# Generated by Django 4.0.2 on 2023-04-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
