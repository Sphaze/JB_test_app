# Generated by Django 4.0.5 on 2022-06-30 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_recorder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='clarify_issue',
        ),
        migrations.RemoveField(
            model_name='post',
            name='closure_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='containment_action',
        ),
        migrations.RemoveField(
            model_name='post',
            name='corrective_action',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description_of_issue',
        ),
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.RemoveField(
            model_name='post',
            name='issue_affects_other_areas',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ncr',
        ),
        migrations.RemoveField(
            model_name='post',
            name='prevented_reoccurence',
        ),
        migrations.RemoveField(
            model_name='post',
            name='root_cause_of_issue',
        ),
        migrations.RemoveField(
            model_name='post',
            name='validation_action',
        ),
    ]