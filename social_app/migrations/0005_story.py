# Generated by Django 3.2.16 on 2023-01-19 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_app', '0004_alter_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, unique=True)),
                ('content_story', models.TextField()),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_story', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
