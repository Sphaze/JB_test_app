# Generated by Django 4.0.5 on 2022-07-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_recorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downtime',
            field=models.DurationField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='est_completion_time',
            field=models.DurationField(default=''),
        ),
    ]
