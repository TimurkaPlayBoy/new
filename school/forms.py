from django import forms
from .models import Class, Uroks, Teacher, Student, Grade, Schedule

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

class UroksForm(forms.ModelForm):
    class Meta:
        model = Uroks
        fields = ['name']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'school_class']  # виправлено: full_name → name

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'uroks', 'value']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['school_class', 'uroks', 'teacher', 'day_of_week', 'lesson_number']