# Generated by Django 4.0.5 on 2022-07-01 14:25

import data_recorder.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ncr_number', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('1', 'Location A'), ('2', 'Location B'), ('3', 'Location C')], max_length=1)),
                ('area_of_issue', models.CharField(choices=[('1', 'A1'), ('2', 'A2'), ('3', 'A3')], max_length=1)),
                ('job_ref_number', models.CharField(max_length=100)),
                ('supervisor_team', models.CharField(max_length=100)),
                ('person_responsible', models.CharField(max_length=100)),
                ('cost', models.PositiveIntegerField()),
                ('est_completion_time', data_recorder.models.CustomDurationField(verbose_name='Completion time: D H:M:S')),
                ('downtime', data_recorder.models.CustomDurationField(verbose_name='Downtime: D H:M:S')),
                ('issue_resolved', models.CharField(choices=[('A', 'YES'), ('B', 'NO')], default='A', max_length=1)),
                ('description_of_issue', models.TextField(default='', null=True)),
                ('root_cause_of_issue', models.TextField(default='', null=True)),
                ('containment_action', models.TextField(default='', null=True)),
                ('corrective_action', models.TextField(default='', null=True)),
                ('validation_action', models.TextField(default='', null=True)),
                ('issue_affects_other_areas', models.CharField(choices=[('A', 'YES'), ('B', 'NO')], default='B', max_length=1)),
                ('clarify_issue', models.TextField(blank=True, default='', null=True)),
                ('prevented_reoccurence', models.CharField(choices=[('A', 'YES'), ('B', 'NO')], default='A', max_length=1)),
                ('closure_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('images', models.TextField(default='', null=True)),
                ('ncr', models.TextField(default='', null=True)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
