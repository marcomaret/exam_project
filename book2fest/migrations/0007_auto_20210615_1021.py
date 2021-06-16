# Generated by Django 3.1.7 on 2021-06-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book2fest', '0006_auto_20210615_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.AddField(
            model_name='artist',
            name='path',
            field=models.FilePathField(default='static/images/default.png', path='static/images/artist'),
        ),
        migrations.AddField(
            model_name='service',
            name='path',
            field=models.FilePathField(default='static/images/default.png', path='static/images/icon'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
