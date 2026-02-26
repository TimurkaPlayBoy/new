from rest_framework import routers
from django.urls import path, include
from .views import UroksViewSet, TeacherViewSet, ClassViewSet, StudentViewSet, ScheduleViewSet, GradeViewSet

router = routers.DefaultRouter()
router.register(r'uroks', UroksViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]