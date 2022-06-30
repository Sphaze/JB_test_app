from django.contrib import admin
from django.utils.html import format_html
from .forms import JBForm
from .models import Post
# Register your models here.
admin.site.register(Post)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
# #    empty_value_display = '-empty-'

#     exclude = ['clarify_issue']
#     readonly_fields = ['clarify_issue_readonly']
    
#     @admin.display(description='ISSUE CLARIFIED (READONLY)')
#     def clarify_issue_readonly(self, obj):
#         return format_html('<textarea cols="80" rows="10" readonly>{}</textarea>', obj.clarify_issue)

# unused code
#def get_form(self, request, obj=None, **kwargs):
#       form = super(JBForm, self).get_form(request, obj, **kwargs)
#       form.base_fields['ncr_number'].required = False
