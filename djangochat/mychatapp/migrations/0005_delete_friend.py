# Generated by Django 4.0.2 on 2023-04-28 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0004_alter_chatmessage_msg_receiver_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
