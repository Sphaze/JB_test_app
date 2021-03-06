from django.contrib import admin
from django.utils.html import format_html
from .forms import JBForm
from .models import Post
from django.apps import apps
from django import forms

# Register your models here.
# admin.site.register(Post)
# admin.site.register(apps.all_models['data_recorder'].values()) #register multiple models


admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):

    exclude = ('est_completion_time', 'downtime') # hide these fields by excluding them
    readonly_fields = ('est_completion_time_readonly', 'downtime_readonly') # display these new fields as readonly

   # html_title = "d = days&nbsp;&nbsp;&nbsp;&nbsp;h = hours&nbsp;&nbsp;&nbsp;&nbsp;m = minutes<br></br>"

    @admin.display(description="Duration of estimated completion time")
    def est_completion_time_readonly(self, obj):
            
        str_output = str(obj.est_completion_time)
        str_output_list = str_output.split(':')

        modify_hour_string = str_output_list[0] # this portion of text will include hours and any days

        if(len(modify_hour_string) == 1): # if there were any days, the length of this portion will be greater than one

            hour_num = modify_hour_string[0] # there were no days, we take the charAt 0 to get hours
        else:
            hour_num = modify_hour_string[len(modify_hour_string)-1] #capture the hour number (the number to the left of the colon which is len(string) - 1)
    
        if  hour_num == "1": #if hours is one, print "hour"
            str_choice_hr = " hour "
        else:
            str_choice_hr = " hours "

        if  str_output_list[1] == "01": #if minutes is one, print "minute"
            str_choice_min = " minute"
        else:
            str_choice_min = " minutes"

        formatted_str = str_output_list[0] + str_choice_hr + str_output_list[1] + str_choice_min  # any days will be automatically shown because of the ISO time format
      
        return format_html('<textarea id="1" cols="40" rows="1" readonly>{}</textarea>', formatted_str)

    @admin.display(description="Duration of downtime")
    def downtime_readonly(self, obj):

        str_output = str(obj.downtime)
        str_output_list = str_output.split(':')

        modify_hour_string = str_output_list[0] # this portion of text will include hours and any days

        if(len(modify_hour_string) == 1): # if there were any days, the length of this portion will be greater than one

            hour_num = modify_hour_string[0] # there were no days, we take the charAt 0 to get hours
        else:
            hour_num = modify_hour_string[len(modify_hour_string)-1] #capture the hour number (the number to the left of the colon which is len(string) - 1)
    
        if  hour_num == "1": #if hours is one, print "hour"
            str_choice_hr = " hour "
        else:
            str_choice_hr = " hours "

        if  str_output_list[1] == "01": #if minutes is one, print "minute"
            str_choice_min = " minute"
        else:
            str_choice_min = " minutes"

        formatted_str = str_output_list[0] + str_choice_hr + str_output_list[1] + str_choice_min  # any days will be automatically shown because of the ISO time format
      
        return format_html('<textarea id="1" cols="40" rows="1" readonly>{}</textarea>', formatted_str)

    # unused code
    #spare = []
    #spare.append("first element data")
    #spare.append("second element data")

    # @admin.display(description="Test:")
    # def items(self):
    #     return format_html('<span>{}<br></br>{}</span>',self.spare[0], self.spare[1])