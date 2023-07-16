from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from django.forms import formset_factory
from django.contrib.auth.hashers import make_password


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Handle the selected role as needed
                # Redirect the user to the appropriate page
                return redirect('home_page')
    else:
        form = forms.LoginForm()

    return render(request, 'student/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = forms.StudentRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('home_page')
    else:
        form = forms.StudentRegistration()
    return render(request, 'student/register.html', {'form': form})

