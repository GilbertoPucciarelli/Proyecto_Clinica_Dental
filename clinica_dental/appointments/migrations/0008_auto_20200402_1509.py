# Generated by Django 3.0.4 on 2020-04-02 19:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_auto_20200401_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultations',
            name='appointment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointments.Appointments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultations',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultations',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]