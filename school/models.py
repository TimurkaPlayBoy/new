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