# Generated by Django 3.1.7 on 2021-06-15 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book2fest', '0014_auto_20210615_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_user', to='book2fest.organizerprofile'),
        ),
    ]
