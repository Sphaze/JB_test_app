from django import forms
from django.forms import ModelForm
from .models import Post

class JBForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = (
        'date_posted', 
        'ncr_number', 
        'location', 
        'area_of_issue', 
        'job_ref_number', 
        'supervisor_team', 
        'person_responsible',
        'cost', 
        'est_completion_time',
        'downtime',
        'issue_resolved',
        # 'description_of_issue',
        # 'root_cause_of_issue',
        # 'containment_action',
        # 'corrective_action',
        # 'validation_action',
        # 'issue_affects_other_areas',
        # 'clarify_issue',
        # 'prevented_reoccurence',
        # 'closure_date',
        # 'images',
        # 'ncr',
        'author'
        )
    
        widgets = {
            'date_posted': forms.DateInput(attrs={'class' : 'form-control'}),
            'ncr_number': forms.TextInput(attrs={'class' : 'form-control', 'Placeholder' : 'NCR Number'}),
            'location': forms.Select(attrs={'class' : 'form-control'}),
            'area_of_issue': forms.Select(attrs={'class' : 'form-control'}),
            'job_ref_number': forms.TextInput(attrs={'class' : 'form-control', 'Placeholder' : 'Job Reference Number'}),
            'supervisor_team':  forms.TextInput(attrs={'class' : 'form-control', 'Placeholder' : 'Supervisor Team'}),
            'person_responsible': forms.TextInput(attrs={'class' : 'form-control', 'Placeholder' : 'Person Responsible'}),
            'cost': forms.NumberInput(attrs={'class' : 'form-control', 'Placeholder' : 'Cost (in pounds)'}),
            'est_completion_time': forms.NumberInput(attrs={'class' : 'form-control', 'Placeholder' : 'Estimated Completion Time (in minutes)'}),
            'downtime': forms.NumberInput(attrs={'class' : 'form-control', 'Placeholder' : 'Estimated Downtime (in minutes)'}),
            'issue_resolved': forms.Select(attrs={'class' : 'form-control'}),
            'description_of_issue': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Description of the issue', 'rows': 2, 'maxlength' : '500'}),
            'root_cause_of_issue': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Root Cause of the issue', 'rows': 2, 'maxlength' : '500'}), 
            'containment_action': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Interim Containment action', 'rows': 2, 'maxlength' : '500'}), 
            'corrective_action': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Corrective Action', 'rows': 2, 'maxlength' : '500'}), 
            'validation_action': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Result of Validation action', 'rows': 2, 'maxlength' : '500'}), 
            'issue_affects_other_areas': forms.Select(attrs={'class' : 'form-control'}),
            'clarify_issue': forms.Textarea(attrs={'class' : 'form-control', 'rows': 2, 'maxlength' : '500'}), 
            'prevented_reoccurence': forms.Select(attrs={'class' : 'form-control'}),
            'closure_date': forms.DateInput(attrs={'class' : 'form-control'}), 
            'images': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Please paste links to images', 'rows': 5, 'maxlength' : '800'}),
            'ncr': forms.Textarea(attrs={'class' : 'form-control', 'Placeholder' : 'Provide hyperlinks to stored location where images are stored with job reference numbers.', 'rows': 5, 'maxlength' : '500'}),
            'author': forms.Select(attrs={'class' : 'form-control'})
            }
        

        labels = {
            'date_posted' : '',
            'ncr_number': '',
            'location': 'Location',
            'area_of_issue': 'Area of Issue',
            'job_ref_number': '',
            'supervisor_team': '',
            'person_responsible': '',
            'cost': '',
            'est_completion_time': '',
            'downtime': '',
            'issue_resolved': 'Was the issue resolved?',
            'description_of_issue': '',
            'root_cause_of_issue': '',
            'containment_action': '',
            'corrective_action': '',
            'validation_action': '',
            'issue_affects_other_areas': 'Does the issue affect any other areas?',
            'clarify_issue': 'If yes, please clarify the issue',
            'prevented_reoccurence': 'Prevented re-occurence of the problem?',
            'closure_date': '',
            'images': '',
            'ncr': 'NCR',
            'author': ''
        }