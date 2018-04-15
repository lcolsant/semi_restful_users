# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from .models import UserManager


def index(request):
    print 'hit index route'
    return redirect('/users')

def users(request):
    context = {
        'all_users': User.objects.all()
    }

    print context['all_users']
    return render(request, 'users/users.html',context)


def new_user(request):
    return render(request, 'users/create.html')

def create(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    
    #validate user input
    erros = User.objects.validate(request,fname,lname,email)
    if len(erros) > 0:
        print 'invalid input'
        for error in erros.itervalues():
            print error
        return redirect('/users/new')

    #else if valid user input, run database query
    User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'])        

    return redirect('/users')


def show(request,id):
    context = {
        'user':User.objects.get(id=id)
    }

    return render(request,'users/show.html', context)


def edit(request,id):
    context = {
        'user':User.objects.get(id=id)
    }
    return render(request,'users/edit.html', context)


def destroy(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')

def update(request,id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']
    user.email = request.POST['email']
    user.save()
    return redirect('/users')