# Generated by Django 3.0.4 on 2020-03-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0002_auto_20200330_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultations',
            name='price',
            field=models.CharField(max_length=5),
        ),
    ]
