from django import forms

from student.models import Student

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group


class LoginForm(AuthenticationForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label='Select a role')


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["username", "password", "email", "ic", "namaPenuh", "umur"]


class StudentLogin(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["username", "password"]