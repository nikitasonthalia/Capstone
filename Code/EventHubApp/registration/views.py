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
from EventHubApp.search.models import User, UserProfile, Category
from django.contrib import messages


categoryName = Category.objects.order_by("category_name")


# Displays registerServiceDetails.html
def registerServiceDetails(request):
    userCategories = Category.objects.exclude(
        category_id__in=UserProfile.objects.filter(user_id=1).values_list('category_id', flat=True))
    template = loader.get_template('registerServiceDetails.html')
    context = {

    }
    return render(request, 'registerServiceDetails.html', {'userCategories': userCategories, 'categoryName': categoryName})

"""def registerServiceDetails(request):
    if request.user.is_authenticated():
        userCategories = Category.objects.exclude(
            category_id__in=UserProfile.objects.filter(user_id=1).values_list('category_id', flat=True))
        template = loader.get_template('registerServiceDetails.html')
        context = {

        }
        return render(request, 'registerServiceDetails.html',
                      {'userCategories': userCategories, 'categoryName': categoryName})
    else:
        messages.warning(request, 'Please correct the error below.')
        return render(request, "registerServiceDetails.html")"""


# Create your views here.
def saveCategory(newCat):
    categoryInstance = Category()
    categoryInstance.category_name = newCat
    categoryInstance.description = newCat
    categoryInstance.category_url = newCat
    categoryInstance.save()


def saveUserProfile(request):
    if 'userid' in request.session:
        userid = request.session.get('userid')
    else:
        userid = 0
    categoryFlag = 0
    profileDetails = UserProfile()
    serviceCategory = request.POST.get('category')
    if serviceCategory == 'Other':
        newCat = request.POST.get('newCategory')
        saveCategory(newCat)

        categoryInfo = Category.objects.get(category_name=newCat)
        profileDetails.category_id = categoryInfo.category_id
        profileDetails.profile_name = newCat
        profileDetails.description = newCat
    else:
        categoryFlag = 1
        categoryDetails = Category.objects.get(category_name=serviceCategory)
        profileDetails.category_id = categoryDetails.category_id
        profileDetails.profile_name = categoryDetails.category_name
        profileDetails.description = categoryDetails.category_name

    # userDetails = User.objects.all()
#     userDetails = User.objects.get(username='Amruta')
    profileDetails.user_id = userid

    # if not os.path.exists("EventHubApp/static/events/assets/img/media/" + "Test"):
    # os.makedirs("EventHubApp/static/events/assets/img/media/" + "Test")

    fs = FileSystemStorage()

    pic1 = request.FILES.get('pic1')
    pic2 = request.FILES.get('pic2')
    pic3 = request.FILES.get('pic3')
    pic4 = request.FILES.get('pic4')
    pic5 = request.FILES.get('pic5')

    if pic1:
        userPic1 = request.FILES['pic1']
        fs.save(userPic1.name, userPic1)
        profileDetails.pic1 = userPic1.name
    if pic2:
        userPic2 = request.FILES['pic2']
        fs.save(userPic2.name, userPic2)
        profileDetails.pic2 = userPic2.name
    if pic3:
        userPic3 = request.FILES['pic3']
        fs.save(userPic3.name, userPic3)
        profileDetails.pic3 = userPic3.name
    if pic4:
        userPic4 = request.FILES['pic4']
        fs.save(userPic4.name, userPic4)
        profileDetails.pic4 = userPic4.name
    if pic5:
        userPic5 = request.FILES['pic5']
        fs.save(userPic5.name, userPic5)
        profileDetails.pic5 = userPic5.name

    profileDetails.price = float(request.POST.get('sprice'))

    profileDetails.save()

    SPDetails = Userprofiledetails()

    if categoryFlag == 1:
        categoryDetails = Category.objects.get(category_name=serviceCategory)
    else:
        categoryDetails = Category.objects.get(category_name=request.POST.get('newCategory'))

    SPDetails.profile = UserProfile.objects.get(user_id=userid, category_id=categoryDetails.category_id)
    SPDetails.serviceName = request.POST.get('sname')
    SPDetails.type = request.POST.get('stype')
    SPDetails.offers = request.POST.get('soffer')
    SPDetails.package = request.POST.get('spackage')
    SPDetails.serviceDetails = request.POST.get('sdetails')
    SPDetails.productDescription = request.POST.get('sdesc')
    SPDetails.aboutProduct = request.POST.get('sprod')
    SPDetails.aboutUs = request.POST.get('sabout')
    SPDetails.save()

    return render(request, 'home.html', {'categoryName': categoryName})

