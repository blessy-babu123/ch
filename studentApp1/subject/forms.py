from django import forms
from .models import Subject

class subjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'subCode']