from rest_framework import viewsets
from .models import Uroks, Teacher, Class, Student, Schedule, Grade
from .serializers import (
    UroksSerializer, TeacherSerializer, ClassSerializer, StudentSerializer,
    ScheduleSerializer, GradeSerializer
)
from django.shortcuts import render
from .models import Schedule, Grade

def index(request):
    return render(request, 'school/index.html')

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'school/schedule_list.html', {'schedules': schedules})

def grades_list(request):
    grades = Grade.objects.all()
    return render(request, 'school/grades_list.html', {'grades': grades})

class UroksViewSet(viewsets.ModelViewSet):
    queryset = Uroks.objects.all()
    serializer_class = UroksSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer