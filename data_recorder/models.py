import datetime
from mimetypes import init
from django.db import models
from django.db.models import DurationField
from django.forms import HiddenInput
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import duration
from django.utils.duration import _get_duration_components
from django.utils.dateparse import parse_duration
from data_recorder.templatetags import custom_filters
from django import forms


# def duration_string(duration):
#     """Version of str(timedelta) which is not English specific."""
#     days, hours, minutes = _get_duration_components(duration)

#     string = "{} days, {} hours, {:02d} minutes".format(days, hours, minutes)

#     return string


class CustomDurationField(DurationField):

    #override this function
    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, datetime.timedelta):
            val = value * 60
            return val
        try:
            parsed = parse_duration(val)
        except ValueError:
            pass
        else:
            if parsed is not None:
                return parsed
        

class control_field(models.TextChoices):
    YES = 'A', 'YES'
    NO = 'B', 'NO'


class control_field_2(models.TextChoices):
    YES = 'A', 'YES'
    NO = 'B', 'NO'
    

class Post(models.Model):

    LOCATION = (
        ('1', 'Location A'),
        ('2', 'Location B'),
        ('3', 'Location C'),
    )

    AREA_OF_ISSUE = (
        ('1', 'A1'),
        ('2', 'A2'),
        ('3', 'A3'),
    ) 

    # Each model field in django each automatically get their own primary key ID (django feature)

    date_posted = models.DateTimeField(default=timezone.now)
    ncr_number = models.CharField(max_length=100)
    location = models.CharField(max_length=1, choices=LOCATION)
    area_of_issue = models.CharField(max_length=1, choices=AREA_OF_ISSUE)
    job_ref_number = models.CharField(max_length=100)
    supervisor_team = models.CharField(max_length=100)
    person_responsible = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    est_completion_time = CustomDurationField("Completion time: D H:M:S", default="") # altered method "duration_string" at django.utils.duration
    downtime = CustomDurationField("Downtime: D H:M:S", default="")
    issue_resolved = models.CharField(max_length=1, choices=control_field.choices, default=control_field.YES)
    description_of_issue = models.TextField(null=True, default="")
    root_cause_of_issue = models.TextField(null=True, default="")
    containment_action = models.TextField(null=True, default="")
    corrective_action = models.TextField(null=True, default="")
    validation_action = models.TextField(null=True, default="")
    issue_affects_other_areas = models.CharField(max_length=1, choices=control_field_2.choices, default=control_field_2.NO)
    clarify_issue = models.TextField(null=True, blank=True, default="") # optional field
    prevented_reoccurence = models.CharField(max_length=1, choices=control_field.choices, default=control_field.YES)
    closure_date = models.DateTimeField(default=timezone.now)
    images = models.TextField(null=True, default="")
    ncr = models.TextField(null=True, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE,default="") #if a user is deleted, delete their entry as well


    #this is called a dunder method (double underscore method)
    def __str__(self):  
        return self.ncr_number # this will create the name for the database entries in the admin page
