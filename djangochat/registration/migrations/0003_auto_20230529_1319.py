# Generated by Django 3.2.9 on 2023-05-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20230509_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='unidad',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]