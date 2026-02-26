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