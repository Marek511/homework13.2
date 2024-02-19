from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)


def password_reset(request):
    return PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    )(request)


def password_reset_done(request):
    return PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    )(request)


def password_reset_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/reset/done/'
    )(request, uidb64=uidb64, token=token)


def password_reset_complete(request):
    return PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    )(request)


def signup_user(request):

    if request.user.is_authenticated:
        return redirect(to='quotes:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def login_user(request):

    if request.user.is_authenticated:
        return redirect(to='quotes:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required
def logout_user(request):
    logout(request)
    return redirect(to='quotes:main')
