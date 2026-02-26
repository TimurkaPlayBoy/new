from rest_framework import viewsets
from .models import Uroks, Teacher, Class, Student, Schedule, Grade
from .serializers import (
    UroksSerializer, TeacherSerializer, ClassSerializer, StudentSerializer,
    ScheduleSerializer, GradeSerializer
)
from django.shortcuts import render
from .models import Schedule, Grade
from django.shortcuts import render, redirect
from .forms import GradeForm, ScheduleForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Grade, Schedule

def grades_list(request):
    query = request.GET.get('q')
    if query:
        grades = Grade.objects.filter(
            Q(student__full_name__icontains=query) |
            Q(uroks__name__icontains=query)
        )
    else:
        grades = Grade.objects.all()
    return render(request, 'school/grades_list.html', {'grades': grades, 'query': query})

def schedule_list(request):
    query = request.GET.get('q')
    if query:
        schedules = Schedule.objects.filter(
            Q(school_class__name__icontains=query) |
            Q(uroks__name__icontains=query) |
            Q(teacher__full_name__icontains=query)
        )
    else:
        schedules = Schedule.objects.all()
    return render(request, 'school/schedule_list.html', {'schedules': schedules, 'query': query})

# --- Grades ---
def edit_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'school/add_grade.html', {'form': form})

def delete_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    grade.delete()
    return redirect('grades_list')

# --- Schedule ---
def edit_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'school/add_schedule.html', {'form': form})

def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    schedule.delete()
    return redirect('schedule_list')


def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades_list')
    else:
        form = GradeForm()
    return render(request, 'school/add_grade.html', {'form': form})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'school/add_schedule.html', {'form': form})

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