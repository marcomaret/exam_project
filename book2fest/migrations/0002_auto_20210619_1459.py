# Generated by Django 3.2.4 on 2021-06-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book2fest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventprofile',
            name='cap',
            field=models.CharField(default='42123', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventprofile',
            name='province',
            field=models.CharField(default='RE', max_length=2),
            preserve_default=False,
        ),
    ]