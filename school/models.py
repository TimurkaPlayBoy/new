from django.db import models


class Uroks(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Uroks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=255)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Schedule(models.Model):
    uroks = models.ForeignKey(Uroks, on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    lesson_number = models.IntegerField()

    def __str__(self):
        return f"{self.school_class} - {self.uroks}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    uroks = models.ForeignKey(Uroks, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.value}"