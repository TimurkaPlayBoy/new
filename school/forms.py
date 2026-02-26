from django import forms
from .models import Grade, Schedule

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'uroks', 'value']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['school_class', 'uroks', 'teacher', 'day_of_week', 'lesson_number']