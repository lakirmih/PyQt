from django import forms
from .models import Student, Lesson

class AttendanceForm(forms.Form):
    student = forms.ModelChoiceField(queryset = Student.objects.all())
    lesson = forms.ModelChoiceField(qeryset = Lesson.objects.all())
