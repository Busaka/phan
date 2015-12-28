
from django import forms
from .models import Job


class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['sch_name', 'subj', 'jmessage']
