from rest_framework import viewsets
from .models import Uroks, Teacher, Class, Student, Schedule, Grade
from .serializers import (
    UroksSerializer, TeacherSerializer, ClassSerializer, StudentSerializer,
    ScheduleSerializer, GradeSerializer
)

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