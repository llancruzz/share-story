# Generated by Django 3.2.16 on 2023-01-19 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0006_sharestory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='traveler',
        ),
        migrations.DeleteModel(
            name='ShareStory',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
