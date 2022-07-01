from django import template

#from django.template.defaulttags import register


register = template.Library()

# @register.filter
# def duration(td):
#     total_seconds = int(td.total_seconds())
#     days = total_seconds // 86400 # total seconds in a day = 86400
#     hours = total_seconds // 3600 # total seconds in an hour = 3600
#     minutes = (total_seconds % 3600) // 60

#     return '{} days {} hours {} min'.format(days, hours, minutes)

#in HTML script do this: {% load custom_filters %}


