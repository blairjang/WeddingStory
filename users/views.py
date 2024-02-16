from django.shortcuts import render, redirect, get_object_or_404
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create(
                                            user_id=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            name=request.POST['name'])
            auth.login(request, user)
            return redirect('/')
        # return render(request, "users/signup.html")
    return render(request, "users/signup.html")




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        user = auth.authenticate(request, user_id=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            
            return render(request, 'users/login.html', {'error' : '회원명이나 비밀번호가 틀립니다'})
        
    return render(request, 'users/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'users/login.html') 



