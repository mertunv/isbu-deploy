from .models import *
from django import forms


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'company', 'location', 'type', 'job_category', 'job_description']
        widgets = {'job_category':forms.RadioSelect}


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = []


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'company', 'location', 'type', 'job_category', 'job_description']
        widgets = {'job_category':forms.RadioSelect}