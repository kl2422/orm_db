from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=20, default='')
    birth = models.DateField()
    gender_choices = [
        (0, '女'),
        (1, '男'),
    ]
    gender = models.IntegerField(choices=gender_choices)
    is_married_choices = [
        (0, '未婚'),
        (1, '已婚'),
    ]
    is_married = models.IntegerField(choices=is_married_choices)


class Student(models.Model):
    name = models.CharField(max_length=20, default='')
    birth = models.DateField()
    gender_choices = [
        (0, '女'),
        (1, '男'),
    ]
    gender = models.IntegerField(choices=gender_choices)
    teachers = models.ManyToManyField(Teacher)
