from django.contrib import admin
from django.utils.html import format_html
from .forms import JBForm
from .models import Post
from django.apps import apps
from django import forms

# Register your models here.
# admin.site.register(Post)
# admin.site.register(apps.all_models['data_recorder'].values()) #register multiple models


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    exclude = ('est_completion_time', 'downtime') # hide these fields by excluding them
    readonly_fields = ('est_completion_time_readonly', 'downtime_readonly') # display these new fields as readonly

    @admin.display(description="Duration of estimated completion time")
    def est_completion_time_readonly(self, obj):
            
        str_output = str(obj.est_completion_time)
        str_output_list = str_output.split(':')

        formatted_str = str_output_list[0] + " hours " + str_output_list[1] + " minutes" # any days will be included from the "duration_string" function

        return formatted_str
        # return format_html('<textarea id="1" cols="60" rows="1" style="width: 610px" readonly>{}</textarea>', formatted_str)


    @admin.display(description="Duration of downtime")
    def downtime_readonly(self, obj):

        str_output = str(obj.downtime)
        str_output_list = str_output.split(':')

        formatted_str2 = str_output_list[0] + " hours " + str_output_list[1] + " minutes" # any days will be included from the "duration_string" function

        return formatted_str2
        # return format_html('<textarea id="1" cols="60" rows="1" style="width: 610px" readonly>{}</textarea>', formatted_str2)
    

    # unused code
    #spare = []
    #spare.append("first element data")
    #spare.append("second element data")

    # @admin.display(description="Test:")
    # def items(self):
    #     return format_html('<span>{}<br></br>{}</span>',self.spare[0], self.spare[1])
  
  