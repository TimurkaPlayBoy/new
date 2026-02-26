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
from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, Uroks, Teacher, Student
from .forms import ClassForm, UroksForm, TeacherForm, StudentForm

# --- Class ---
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'school/class_list.html', {'classes': classes})

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'school/add_class.html', {'form': form})

def edit_class(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    form = ClassForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('class_list')
    return render(request, 'school/add_class.html', {'form': form})

def delete_class(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    obj.delete()
    return redirect('class_list')


# --- Uroks ---
def uroks_list(request):
    uroks = Uroks.objects.all()
    return render(request, 'school/uroks_list.html', {'uroks': uroks})

def add_uroks(request):
    if request.method == 'POST':
        form = UroksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uroks_list')
    else:
        form = UroksForm()
    return render(request, 'school/add_uroks.html', {'form': form})

def edit_uroks(request, pk):
    obj = get_object_or_404(Uroks, pk=pk)
    form = UroksForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('uroks_list')
    return render(request, 'school/add_uroks.html', {'form': form})

def delete_uroks(request, pk):
    obj = get_object_or_404(Uroks, pk=pk)
    obj.delete()
    return redirect('uroks_list')


# --- Teacher ---
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'school/add_teacher.html', {'form': form})

def edit_teacher(request, pk):
    obj = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'school/add_teacher.html', {'form': form})

def delete_teacher(request, pk):
    obj = get_object_or_404(Teacher, pk=pk)
    obj.delete()
    return redirect('teacher_list')


# --- Student ---
def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'school/add_student.html', {'form': form})

def edit_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'school/add_student.html', {'form': form})

def delete_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect('student_list')

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