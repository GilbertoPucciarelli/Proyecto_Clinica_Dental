# Generated by Django 3.0.4 on 2020-03-10 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bloqued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]
