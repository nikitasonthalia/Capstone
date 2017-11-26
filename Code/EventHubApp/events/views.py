from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.shortcuts import render_to_response
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
# from .gmaps import gMapfun
# from .paint import paintDraw
import importlib.util
import sys
from .models import *
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
#Import Folder model
#from filer.models.foldermodels import Folder
from EventHubApp.search.models import User, UserProfile, Category
from django.contrib.auth.models import User as DUser
from django.contrib.auth import authenticate

categoryName = Category.objects.order_by("category_name")[:12]



# def index(request):
#    return HttpResponse("Hello Amruta. You're at the polls index.")

# def index(request):
#     template = loader.get_template('events/home.html')
#     context = {
#     }
#     return HttpResponse(template.render(context, request))

# Displays home.html
def home(request):
    template = loader.get_template('home.html')
    # categoryName = Category.objects.order_by("category_name")
    context = {

    }
    # userName = User.objects.filter(username='Amruta')
    # return HttpResponse(template.render(context, request))
    return render(request, 'home.html', {'categoryName': categoryName})


# Displays florist.html
def florist(request):
    template = loader.get_template('florist.html')
    context = {

    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'florist.html', {'categoryName': categoryName})


# Displays florist1.html
def florist1(request):
    template = loader.get_template('florist1.html')
    context = {

    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'florist1.html', {'categoryName': categoryName})

# Displays contact.html
def contact(request):
    template = loader.get_template('contact.html')
    context = {

    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'contact.html', {'categoryName': categoryName})

# Display aboutUs.html
def aboutUs(request):
    template = loader.get_template('aboutUs.html')
    context = {

    }
    return render(request, 'aboutUs.html')

# save Contact Us Form
def contactUs(request):
    contactInstance = Contact()

    #userDetails = User.objects.get(username='Amruta')
    contactInstance.userid = 1
    contactInstance.email = request.POST.get('emailId')
    contactInstance.reason = request.POST.get('reason')
    contactInstance.messsage = request.POST.get('message')
    contactInstance.save()
    return render(request, 'contactConfirmation.html')

# Displays register.html
"""def register(request):
    template = loader.get_template('events/register.html')
    #form = ServiceProvidersForm()
    context = {

    }
    #return render(request, 'events/register.html', {'categoryName': categoryName, 'form': form})
    return render(request, 'events/register.html', {'categoryName': categoryName})

# Displays registerServiceDetails.html
def registerServiceDetails(request):
    template = loader.get_template('events/registerServiceDetails.html')
    context = {

    }
    return render(request, 'events/registerServiceDetails.html', {'categoryName': categoryName})"""


# Registration Form
"""def getForm(request):
    serviceProiderInstance = ServiceProviders()
    serviceProiderInstance.title = request.POST.get('title')
    serviceProiderInstance.inputFname = request.POST.get('inputFname')
    serviceProiderInstance.inputLname = request.POST.get('inputLname')
    serviceProiderInstance.emailId = request.POST.get('emailId')
    serviceProiderInstance.passwd = request.POST.get('passwd')
    serviceProiderInstance.birthDate = request.POST.get('birthday')
    serviceProiderInstance.stadd1 = request.POST.get('stadd1')
    serviceProiderInstance.stadd2 = request.POST.get('stadd2')
    serviceProiderInstance.city = request.POST.get('city')
    serviceProiderInstance.state = request.POST.get('state')
    serviceProiderInstance.zip = request.POST.get('zip')
    serviceProiderInstance.phone = request.POST.get('phone')
    serviceCategory = request.POST.get('category')
    if serviceCategory == 'Other':
        serviceProiderInstance.category = request.POST.get('newCategory')
        serviceProiderInstance.serviceDesc = request.POST.get('newCategory')
    else:
        serviceProiderInstance.category = serviceCategory
        serviceProiderInstance.serviceDesc = serviceCategory


    myfile = request.FILES['pic']
    fs = FileSystemStorage()
    fs.save(myfile.name, myfile)
    serviceProiderInstance.pic = myfile.name

    serviceProiderInstance.save()

    return render(request, 'events/registerServiceDetails.html', {'categoryName': categoryName, 'categoryType': serviceProiderInstance.category})

#Service Details Form
def getServiceDetails(request):
    SPDetails = ServiceProviderDetails()
    SPDetails.spID = "1"
    SPDetails.serviceName = request.POST.get('sname')
    SPDetails.type = request.POST.get('stype')
    SPDetails.offers = request.POST.get('soffer')
    SPDetails.package = request.POST.get('spackage')
    SPDetails.serviceDetails = request.POST.get('sdetails')
    SPDetails.productDescription = request.POST.get('sdesc')
    SPDetails.aboutProduct = request.POST.get('sprod')
    SPDetails.aboutUs = request.POST.get('sabout')
    SPDetails.save()
    return render(request, 'events/home.html')"""
def signin(request):
    name = request.GET['username']
    pwd = request.GET['password']
    # message = 'You entered username : %r' % name
    #message = 'You entered password : %r' % pwd
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
        return render(request, 'home.html', {'categoryName': categoryName})
       

def signup(request):
    template = loader.get_template('signup.html')
    context = {
    }
    return render(request, 'signup.html')

def signupSubmit(request):
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
    userProfile.save()
    return render(request, 'home.html')

