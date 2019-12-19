from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'voting/home.html')


def adminlogin(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == "picsoreel":
            user = authenticate(username="Tanmay", password="picsoreel")
            auth.login(request, user)
            return render(request, 'voting/signup.html')
        return render(request, 'voting/adminlogin.html')
    return render(request, 'voting/adminlogin.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = "picsoreel2k19"
        try:
            User.objects.create_user(username=username, password=password)
        except:
            return render(request, 'voting/signup.html', {'error': 'Username taken'})
        return render(request, 'voting/signup.html')
    return render(request, 'voting/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            find = User.objects.get(username=username)
        except:
            return render(request, 'voting/login.html', {'error': "Incorrect username"})
        user = authenticate(username=username, password="picsoreel2k19")
        if user:
            if user.is_active:
                User.objects.filter(username=username).update(is_active=False)
                auth.login(request, user)
                return JsonResponse({"success": True})
                # return render(request, 'voting/home.html')
        else:
            print(1)
            return render(request, 'voting/login.html')
    else:
        print(2)
        return render(request, 'voting/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
