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

    userProfile = User(first_name=firstname, last_name=lastname, email=email, username=username, password=passwd,
                       street1=street1, street2=street2, city=city, state=state, country=country, pin_number=pin_number,
                       phone=phone)
    userProfile.user_type_id_id = 1
    userProfile.save()
    return render(request, 'home.html', {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})


def account(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()

    if 'userid' in request.session:
        userid = request.session.get('userid')
        username = request.session.get('username')
        print(username)
        print("userid: ", userid)
    else:
        userid = 0
        return render(request, 'home.html', {'list1': list1, 'loginRequired': True})

    userDetails = User.objects.get(user_id=userid)
    profileDetails = UserProfile.objects.filter(user_id=userid)

    if not profileDetails:
        template = loader.get_template('regularUserAccount.html')
        context = {

        }
        return render(request, 'regularUserAccount.html',
                      {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames,
                       'userDetails': userDetails})
    else:
        userCategories = Category.objects.filter(
            category_id__in=UserProfile.objects.filter(user_id=userid).values_list('category_id', flat=True))
        template = loader.get_template('serviceUserAccount.html')
        context = {

        }
        return render(request, 'serviceUserAccount.html',
                      {'list1': list1, 'profileDetails': profileDetails, 'stateNames': stateNames,
                       'cityNames': cityNames,
                       'userDetails': userDetails,'userCategories': userCategories})


def modifyServiceUserProfile(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()

    if 'userid' in request.session:
        userid = request.session.get('userid')
    else:
        userid = 0
        return render(request, 'home.html', {'list1': list1, 'loginRequired': True})

    userInstance = User.objects.get(user_id=userid)

    if request.POST.get('phone'):
        userInstance.phone = request.POST.get('phone')
    if request.POST.get('street1'):
        userInstance.street1 = request.POST.get('street1')
    if request.POST.get('street2'):
        userInstance.street2 = request.POST.get('street2')
    if request.POST.get('cityName'):
        userInstance.city = request.POST.get('cityName')
    if request.POST.get('stateName'):
        userInstance.state = request.POST.get('stateName')
    if request.POST.get('pin'):
        userInstance.pin_number = request.POST.get('pin')

    userInstance.save()

    categoryID = request.POST.get('categoryID')
    profileData = UserProfile.objects.get(user_id=userid, category_id=categoryID)
    profileDetailsData = Userprofiledetails.objects.get(profile_id=profileData.profile_id)
    return render(request, 'serviceProfileUpdate.html',
                  {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames, 'profileData': profileData,
                   'profileDetailsData': profileDetailsData})


def updateUserProfileDetails(request):
    profileID = request.POST.get('pid')
    # print("profile_id:" , profileID)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()

    if 'userid' in request.session:
        userid = request.session.get('userid')
    else:
        userid = 0
        return render(request, 'home.html', {'list1': list1, 'loginRequired': True})

    profileDetailsInstance = Userprofiledetails.objects.get(profile_id=profileID)
    profileInstance = UserProfile.objects.get(profile_id=profileID)

    if request.POST.get('stype'):
        profileDetailsInstance.type = request.POST.get('stype')
    if request.POST.get('soffer'):
        profileDetailsInstance.offers = request.POST.get('soffer')
    if request.POST.get('spackage'):
        profileDetailsInstance.package = request.POST.get('spackage')
    if request.POST.get('sdetails'):
        profileDetailsInstance.servicedetails = request.POST.get('sdetails')
    if request.POST.get('sdesc'):
        profileDetailsInstance.productdescription = request.POST.get('sdesc')
    if request.POST.get('sprod'):
        profileDetailsInstance.aboutproduct = request.POST.get('sprod')
    if request.POST.get('sabout'):
        profileDetailsInstance.aboutus = request.POST.get('sabout')

    profileDetailsInstance.save()

    fs = FileSystemStorage()

    pic1 = request.FILES.get('pic1')
    pic2 = request.FILES.get('pic2')
    pic3 = request.FILES.get('pic3')
    pic4 = request.FILES.get('pic4')
    pic5 = request.FILES.get('pic5')

    if pic1:
        userPic1 = request.FILES['pic1']
        fs.save(userPic1.name, userPic1)
        profileInstance.pic1 = userPic1.name
    if pic2:
        userPic2 = request.FILES['pic2']
        fs.save(userPic2.name, userPic2)
        profileInstance.pic2 = userPic2.name
    if pic3:
        userPic3 = request.FILES['pic3']
        fs.save(userPic3.name, userPic3)
        profileInstance.pic3 = userPic3.name
    if pic4:
        userPic4 = request.FILES['pic4']
        fs.save(userPic4.name, userPic4)
        profileInstance.pic4 = userPic4.name
    if pic5:
        userPic5 = request.FILES['pic5']
        fs.save(userPic5.name, userPic5)
        profileInstance.pic5 = userPic5.name

    profileInstance.save()

    return render(request, 'home.html',
                  {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})


def modifyRegularUserProfile(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()

    if 'userid' in request.session:
        userid = request.session.get('userid')
    else:
        userid = 0
        return render(request, 'home.html', {'list1': list1, 'loginRequired': True})

    userInstance = User.objects.get(user_id=userid)

    if request.POST.get('phone'):
        userInstance.phone = request.POST.get('phone')
    if request.POST.get('street1'):
        userInstance.street1 = request.POST.get('street1')
    if request.POST.get('street2'):
        userInstance.street2 = request.POST.get('street2')
    if request.POST.get('cityName'):
        userInstance.city = request.POST.get('cityName')
    if request.POST.get('stateName'):
        userInstance.state = request.POST.get('stateName')
    if request.POST.get('pin'):
        userInstance.pin_number = request.POST.get('pin')

    userInstance.save()
    return render(request, 'home.html', {'list1': list1, 'stateNames': stateNames, 'cityNames': cityNames})
