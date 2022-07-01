from django.contrib import admin
from django.utils.html import format_html
from .forms import JBForm
from .models import Post
import datetime
# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    exclude = ['est_completion_time'] # hide this database column
    exclude = ['downtime'] # hide this database column

    readonly_fields = ['est_completion_time_readonly']
    readonly_fields = ['downtime_readonly']
    
    @admin.display(description='Duration of estimated completion time')
    def est_completion_time_readonly(self, obj):
        str_output = str(obj.est_completion_time)
        str_output_list = str_output.split(':')

        size_of_list = len(str_output_list)

        if size_of_list == 3:
            formatted_str = str_output_list[0] + " hours " + str_output_list[1] + " minutes"
        else:
            formatted_str = str_output_list[0] + " days " + str_output_list[1] + " hours " + str_output_list[2] + "minutes"
 
        return format_html('<textarea cols="60" rows="1" style="width: 610px" readonly>{}</textarea>', formatted_str)

    
    @admin.display(description='Duration of downtime')
    def downtime_readonly(self, obj):
        str_output = str(obj.downtime)
        str_output_list = str_output.split(':')

        size_of_list = len(str_output_list)

        if size_of_list == 3:
            formatted_str = str_output_list[0] + " hours " + str_output_list[1] + " minutes"
        else:
            formatted_str = str_output_list[0] + " days " + str_output_list[1] + " hours " + str_output_list[2] + "minutes"
 
        return format_html('<textarea cols="60" rows="1" style="width: 610px" readonly>{}</textarea>', formatted_str)


# unused code
#def get_form(self, request, obj=None, **kwargs):
#       form = super(JBForm, self).get_form(request, obj, **kwargs)
#       form.base_fields['ncr_number'].required = False