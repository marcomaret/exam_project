# Generated by Django 3.2.4 on 2021-06-13 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book2fest', '0002_userprofile_organizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='organizer',
        ),
        migrations.CreateModel(
            name='OrganizerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=32)),
                ('short_bio', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organizer_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
