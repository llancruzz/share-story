# Generated by Django 3.2.16 on 2023-01-16 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]
