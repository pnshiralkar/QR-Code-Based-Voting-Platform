from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'voting/home.html')


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username').upper()
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
            if password == "admin":
                user = authenticate(username=username, password="admin")
                auth.login(request, user)
                return render(request, 'voting/signup.html')
            else:
                return render(request, 'voting/adminlogin.html', {'error1': "Invalid password"})
        except:
            return render(request, 'voting/adminlogin.html', {'error2': "Invalid admin"})
        return render(request, 'voting/adminlogin.html')
    return render(request, 'voting/adminlogin.html')


def signup(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            username = request.POST.get('username').upper()
            password = "picsoreel2k19"
            try:
                User.objects.create_user(username=username, password=password)
            except:
                return render(request, 'voting/signup.html', {'error': 'Username taken'})
            return render(request, 'voting/signup.html')
        return render(request, 'voting/adminlogin.html')
    print(request.user.username)
    raise Http404()


def login(request):
    if request.method == "POST":
        username = request.POST.get('username').upper()
        try:
            User.objects.get(username=username)
        except:
            return JsonResponse({"success": False, "status": "Invalid ID ; Make sure you are registered by Pictoreal volunteer."})
        user = authenticate(username=username, password="picsoreel2k19")
        if user:
            if user.is_active:
                User.objects.filter(username=username).update(is_active=False)
                auth.login(request, user)
                return JsonResponse({"success": True})
            return JsonResponse({"success": False, "status": "Duplicate user!"})
        else:
            return JsonResponse({"success": False, "status": "Duplicate user!"})
    else:
        raise Http404()


def logout(request):
    auth.logout(request)
    return redirect('home')
