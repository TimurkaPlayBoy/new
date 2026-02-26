from rest_framework import routers
from school.views import UroksViewSet, TeacherViewSet, ClassViewSet, StudentViewSet, ScheduleViewSet, GradeViewSet
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('school.urls')),  # тут підключаємо router з school
]
router = routers.DefaultRouter()
router.register(r'uroks', UroksViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

# ✅ Ніяких include() всередині цього файлу
urlpatterns = router.urls