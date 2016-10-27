from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from mongoengine.django.auth import User
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        username = data['username']
        password = data['password']
        user = User.objects(username=username).first()
        if user and user.check_password(password):
            request.session['username'] = username
            request.session['role'] = user.role
            return HttpResponse(username)
        else:
            return HttpResponse('Username or password not correct')

    if request.method == 'GET':
        if 'username' in request.session:
            return redirect('/')
        return render(request, 'user/login.html', {})

def logout(request):
    request.session.flush()
    return HttpResponse("logout")

def register(request):
    pass
