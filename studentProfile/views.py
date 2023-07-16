from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from django.forms import formset_factory


# Profile Views
@login_required
def profile(request):
    return render(request, 'studentProfile/profile.html')


# Student Achievement Views Form
def studentAchievement(request):
    Formset = formset_factory(forms.StudentAchievementForm, extra=5)
    if request.method == 'POST':
        formset = Formset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    studentAchievement = form.save(commit=False)
                    studentAchievement.studentID = request.user.student
                    studentAchievement.save()
            return redirect('profile_page')
    else:
        formset = Formset()
    return render(request, 'studentProfile/achievement.html', {'formset': formset})


# Student Grade Views Form
def StudentGrades(request):
    Formset = formset_factory(forms.StudentGradesForm, extra=10)
    eligibility_messages = []
    if request.method == 'POST':
        formset = Formset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    student_grade = form.save(commit=False)
                    student_grade.studentID = request.user.student
                    eligibility_message = student_grade.check_eligibility()
                    eligibility_messages.append(eligibility_message)
                    student_grade.save()
            return render(request, 'studentProfile/result.html', {'eligibility_messages': eligibility_messages})
    else:
        formset = Formset()
    
    return render(request, 'studentProfile/studentGrade.html', {'formset': formset})

