from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.shortcuts import render_to_response
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
import importlib.util
import sys
import os
from .models import *
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# Import Folder model
# from filer.models.foldermodels import Folder
from EventHubApp.search.models import User, UserProfile, Category
from django.contrib.auth.models import User as DUser
from django.contrib.auth import authenticate
from EventHubApp.registration.models import States, Userprofiledetails
from django.core.files.storage import FileSystemStorage



# Displays contact.html
def contact(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    template = loader.get_template('contact.html')
    context = {

    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'contact.html', {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})


# Display aboutUs.html
def aboutUs(request):
    list1 = Category.objects.all()
    template = loader.get_template('aboutUs.html')
    context = {

    }
    return render(request, 'aboutUs.html', {'list1': list1})


# save Contact Us Form
def contactUs(request):
    contactInstance = Contact()

    # userDetails = User.objects.get(username='Amruta')
    contactInstance.userid = 1
    contactInstance.email = request.POST.get('emailId')
    contactInstance.reason = request.POST.get('reason')
    contactInstance.messsage = request.POST.get('message')
    contactInstance.save()
    return render(request, 'contactConfirmation.html')


def signin(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    name = request.GET['username']
    pwd = request.GET['password']
    # message = 'You entered username : %r' % name
    # message = 'You entered password : %r' % pwd
    # return HttpResponse(message)
    #result = User.objects.filter(username=name).exists()
    #return HttpResponse(result)
    try:
        duser = authenticate(username=name, password=pwd)
        print(duser)
        user = User.objects.get(username=name, password = pwd)
    except User.DoesNotExist:
        return render(request,'nologinsuccess.html')
    else:
        request.session["userid"] = user.user_id
        #template = loader.get_template('home.html')
        return render(request, 'home.html')

    # result = User.objects.filter(username=name).exists()
    # return HttpResponse(result)
    user = User.objects.get(username=name, password=pwd);
    if user:
        request.session["userid"] = user.user_id
        request.session["username"] = user.username
        template = loader.get_template('home.html')
        return render(request, 'home.html', {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})
    else:
        return render(request, 'nologinsuccess.html')


def signup(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    template = loader.get_template('signup.html')
    context = {
    }
    return render(request, 'signup.html', {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})


def signupSubmit(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    firstname = request.GET['inputFname']
    lastname = request.GET['inputLname']
    email = request.GET['emailId']
    username = request.GET['username']
    passwd = request.GET['passwd']
    street1 = request.GET['street1']
    street2 = request.GET['street2']
    city = request.GET['city']
    state = request.GET['state']
    country = request.GET['country']
    pin_number = request.GET['pin_number']
    phone = request.GET['phone']
    user = DUser.objects.create_user(firstname, username, passwd)
    user.save()
    userProfile =  User(first_name = firstname, last_name = lastname, email = email, username = username, password = passwd,
                        street1 = street1, street2 = street2, city = city, state = state, country = country, phone = phone)
#     userProfile.user_type_id_id = 1


    userProfile = User(first_name=firstname, last_name=lastname, email=email, username=username, password=passwd,
                       street1=street1, street2=street2, city=city, state=state, country=country, pin_number=pin_number,
                       phone=phone)
    userProfile.user_type_id_id = 1
    userProfile.save()
    return render(request, 'home.html', {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})
