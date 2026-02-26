from django.contrib import admin
from django.urls import path, include
from school.views import (
    UroksViewSet, TeacherViewSet, ClassViewSet,
    StudentViewSet, ScheduleViewSet, GradeViewSet
)
from rest_framework import routers
from django.urls import path
from . import views
# school/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Class
    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.class_add, name='class_add'),
    path('classes/<int:pk>/edit/', views.class_edit, name='class_edit'),
    path('classes/<int:pk>/delete/', views.class_delete, name='class_delete'),

    # Uroks
    path('uroks/', views.uroks_list, name='uroks_list'),
    path('uroks/add/', views.uroks_add, name='uroks_add'),
    path('uroks/<int:pk>/edit/', views.uroks_edit, name='uroks_edit'),
    path('uroks/<int:pk>/delete/', views.uroks_delete, name='uroks_delete'),

    # Teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_add, name='teacher_add'),
    path('teachers/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),

    # Student
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Grade
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_add, name='grade_add'),
    path('grades/<int:pk>/edit/', views.grade_edit, name='grade_edit'),
    path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),

    # Schedule
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedules/add/', views.schedule_add, name='schedule_add'),
    path('schedules/<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
    path('schedules/<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),
]


router = routers.DefaultRouter()
router.register(r'uroks', UroksViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/', include('school.urls')),  # DRF API
]

urlpatterns += [
    path('grades/add/', views.add_grade, name='add_grade'),
    path('schedule/add/', views.add_schedule, name='add_schedule'),
]

urlpatterns += [
    path('grades/edit/<int:pk>/', views.edit_grade, name='edit_grade'),
    path('grades/delete/<int:pk>/', views.delete_grade, name='delete_grade'),
    path('schedule/edit/<int:pk>/', views.edit_schedule, name='edit_schedule'),
    path('schedule/delete/<int:pk>/', views.delete_schedule, name='delete_schedule'),
]

urlpatterns += [
    # Class
    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.add_class, name='add_class'),
    path('classes/edit/<int:pk>/', views.edit_class, name='edit_class'),
    path('classes/delete/<int:pk>/', views.delete_class, name='delete_class'),

    # Uroks
    path('uroks/', views.uroks_list, name='uroks_list'),
    path('uroks/add/', views.add_uroks, name='add_uroks'),
    path('uroks/edit/<int:pk>/', views.edit_uroks, name='edit_uroks'),
    path('uroks/delete/<int:pk>/', views.delete_uroks, name='delete_uroks'),

    # Teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/edit/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),

    # Student
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]