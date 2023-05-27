from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name', 'total_marks']
        # Include other fields as needed