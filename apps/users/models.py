# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    # def validate(self,postData):
    #     errors = {}
    #     if len(postData['first_name']) < 2:
    #         errors["name"] = "Fist name should be more than 1 characters"
    #     if len(postData['email']) < 3:
    #         errors["email"] = "Email should be more than 2 characters"
    #     return errors

    def validate(self,request,fname,lname,email):
        errors = {}
        if len(fname) < 2:
            errors["fname"] = "Fist name should be more than 1 characters"
            messages.error(request,"Fist name should be more than 1 characters")
            print 'invalid first name'
        if len(lname) < 2:
            errors["lname"] = "Last name should be more than 1 characters"
            messages.error(request,"Last name should be more than 1 characters")
            print 'invalid last name'
        if len(email) < 3:
            errors["email"] = "Email should be more than 2 characters"
            messages.error(request,"Email should be more than 2 characters")
            print 'invalid email'
        if not EMAIL_REGEX.match(email):
            errors["email"] = "Invalid email format"
            messages.error(request,"Invalid email address format")
            print 'invalid email format'
            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name,self.last_name,self.email)

