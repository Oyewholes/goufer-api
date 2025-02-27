# Generated by Django 5.0.6 on 2024-06-19 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_gofer_custom_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagePoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='message_poster', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
