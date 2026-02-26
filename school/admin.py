from django.contrib import admin
from .models import Uroks, Teacher, Class, Student, Schedule, Grade


admin.site.register(Uroks)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Grade)