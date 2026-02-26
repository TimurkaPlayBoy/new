from rest_framework import routers
from .views import UroksViewSet, TeacherViewSet, ClassViewSet, StudentViewSet, ScheduleViewSet, GradeViewSet
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from rest_framework import routers
from .views import UroksViewSet, TeacherViewSet, ClassViewSet, StudentViewSet, ScheduleViewSet, GradeViewSet

router = routers.DefaultRouter()
router.register(r'uroks', UroksViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('grades/', views.grades_list, name='grades_list'),
]

urlpatterns += router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('school.urls')),
]
router = routers.DefaultRouter()
router.register(r'uroks', UroksViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = router.urls