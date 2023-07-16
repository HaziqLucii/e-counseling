from django import forms

from student.models import Student
from . import models

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group


class StudentAchievementForm(forms.ModelForm):
    class Meta:
        model = models.StudentAchievement
        fields = ['studentMerit']


class StudentGradesForm(forms.ModelForm):
    class Meta:
        model = models.StudentGrades
        fields = ['studentSubject', 'studentGrade']