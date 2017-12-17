# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def process(request, action):
    if request.method == 'POST':
        if action == 'add':
            check_submission = User.objects.validateRegistration(request.POST)
            if len(check_submission) > 0:
                for message in check_submission['error']:
                    messages.error(request, message)
                return redirect('/')
            else:
                newuser = User.objects.addUser(request.POST)
                print newuser
                request.session['id'] = newuser.id
                return redirect('/welcome/'+ str(newuser.id) +'')
        elif action == 'login':
            if len(request.POST['user_input']) < 1 or len(request.POST['password']) < 8:
                messages.warning(request, 'Invalid login information')
                return redirect('/')
            user = User.objects.validateLogin(request.POST)
            if user:
                request.session['id'] = user
                return redirect('/welcome/'+ str(user) +'')
            else:
                messages.warning(request, 'Invalid login information')
                return redirect('/')
            return redirect('/')
    else:
        print 'get out'
        return redirect('/')

def welcome(request, user_id):
    try:
        request.session['id']
    except:
        return redirect('/')
    if request.session['id'] == int(user_id):
        the_user = User.objects.get(id=request.session['id'])
        return render(request, 'login_registration/welcome.html', {'user': the_user})
    else:
        return redirect('/')