# Generated by Django 3.0.4 on 2020-04-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_auto_20200402_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultations',
            name='price',
            field=models.IntegerField(),
        ),
    ]