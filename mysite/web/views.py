
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm

# Create your views here.
def index(request):
    return render(request, 'web/base.html')


def register_view(request):
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            email = register_form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'web/register.html', {'register_form': register_form})


def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
    return render(request, 'web/login.html', {'login_form': login_form})

@login_required
def member_view(request):
    return render(request, 'web/member.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('web:index'))