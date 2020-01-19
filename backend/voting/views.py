from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect
import operator
from .models import Vote


def home(request):
    return render(request, 'voting/home.html')


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'voting/signup.html')
        except:
            return render(request, 'voting/adminlogin.html', {'error2': "Invalid admin"})
    return render(request, 'voting/adminlogin.html')


def signup(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            username = request.POST.get('username').upper()
            password = "picsoreel2k19"
            try:
                User.objects.create_user(username=username, password=password)
            except:
                return JsonResponse({"success": False, "status": "Username Taken"})
            return JsonResponse({"success": True})
        raise Http404()
    raise Http404()


def login(request):
    if request.method == "POST":
        username = request.POST.get('username').upper()
        try:
            User.objects.get(username=username)
        except:
            return JsonResponse(
                {"success": False, "status": "Invalid ID ; Make sure you are registered by Pictoreal volunteer."})
        user = authenticate(username=username, password="picsoreel2k19")
        if user:
            if user.is_active:
                auth.login(request, user)
                return JsonResponse({"success": True})
            return JsonResponse({"success": False, "status": "Duplicate user!"})
        else:
            return JsonResponse({"success": False, "status": "Duplicate user!"})
    else:
        raise Http404()


def voting(request):
    if request.user.is_authenticated:
        return render(request, 'voting/voting.html')
    else:
        return HttpResponse(status=403)


def submit(request):
    if request.user.is_authenticated:
        s1, s2, s3, p1, p2, p3 = '', '', '', '', '', ''
        try:
            if request.COOKIES['check'] != 'pictoreal':
                raise Http404()
        except:
            raise Http404()
        try:
            s1 = request.COOKIES['s0']
        except:
            pass
        try:
            s2 = request.COOKIES['s1']
        except:
            pass
        try:
            s3 = request.COOKIES['s2']
        except:
            pass

        try:
            p1 = request.COOKIES['p0']
        except:
            pass
        try:
            p2 = request.COOKIES['p1']
        except:
            pass
        try:
            p3 = request.COOKIES['p2']
        except:
            pass
        vote = Vote(IDNumber=request.user.username, drawing1=s1, drawing2=s2, drawing3=s3, photo1=p1, photo2=p2,
                    photo3=p3)
        vote.save()
        User.objects.filter(username=request.user.username).update(is_active=False)
        auth.logout(request)
        response = redirect('thanks')
        response.delete_cookie('user_location')
        return response
    else:
        return HttpResponse(status=403)


def thanks(request):
    return render(request, 'voting/thanks.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def count(request):
    if request.user.is_staff or request.user.is_superuser:
        listp = []
        listd = []
        allVotes = Vote.objects.all()
        for i in allVotes:
            try:
                vote = i
                try:
                    drawing1 = int(vote.drawing1[1:])
                    listd.append(drawing1)
                except:
                    pass
                try:
                    drawing2 = int(vote.drawing2[1:])
                    listd.append(drawing2)
                except:
                    pass
                try:
                    drawing3 = int(vote.drawing3[1:])
                    listd.append(drawing3)
                except:
                    pass
                try:
                    photo1 = int(vote.photo1[1:])
                    listp.append(photo1)
                except:
                    pass
                try:
                    photo2 = int(vote.photo2[1:])
                    listp.append(photo2)
                except:
                    pass
                try:
                    photo3 = int(vote.photo3[1:])
                    listp.append(photo3)
                except:
                    pass
            except:
                continue
        freqp = {}
        try:
            for item in listp:
                if item in freqp:
                    freqp[item] += 1
                else:
                    freqp[item] = 1
        except:
            pass

        freqd = {}
        try:
            for item in listd:
                if item in freqd:
                    freqd[item] += 1
                else:
                    freqd[item] = 1
        except:
            pass

        sortedp = dict(sorted(freqp.items(), key=operator.itemgetter(1), reverse=True))
        sortedd = dict(sorted(freqd.items(), key=operator.itemgetter(1), reverse=True))

        return render(request, 'voting/count.html', {'sortedd': sortedd, 'sortedp': sortedp})
    return HttpResponse("<center><h1>You are not allowed to view this page</h1></center>")
