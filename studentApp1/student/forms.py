from django import forms
from .models import Student,Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'email','photo']
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher 
        fields = ['name', 'age', 'experience','subject','joined_date']
