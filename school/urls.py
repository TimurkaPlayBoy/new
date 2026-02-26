from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # ===== Class =====
    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.class_add, name='class_add'),
    path('classes/<int:pk>/edit/', views.class_edit, name='class_edit'),
    path('classes/<int:pk>/delete/', views.class_delete, name='class_delete'),

    # ===== Uroks =====
    path('uroks/', views.uroks_list, name='uroks_list'),
    path('uroks/add/', views.uroks_add, name='uroks_add'),
    path('uroks/<int:pk>/edit/', views.uroks_edit, name='uroks_edit'),
    path('uroks/<int:pk>/delete/', views.uroks_delete, name='uroks_delete'),

    # ===== Teacher =====
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_add, name='teacher_add'),
    path('teachers/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),

    # ===== Student =====
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # ===== Grade =====
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_add, name='grade_add'),
    path('grades/<int:pk>/edit/', views.grade_edit, name='grade_edit'),
    path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),

    # ===== Schedule =====
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedules/add/', views.schedule_add, name='schedule_add'),
    path('schedules/<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
    path('schedules/<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),
]