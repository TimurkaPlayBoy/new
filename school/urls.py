from django.contrib import admin
from django.urls import path, include
from school.views import (
    UroksViewSet, TeacherViewSet, ClassViewSet,
    StudentViewSet, ScheduleViewSet, GradeViewSet
)
from rest_framework import routers
from django.urls import path
from . import views


router = routers.DefaultRouter()
router.register(r'uroks', UroksViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
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