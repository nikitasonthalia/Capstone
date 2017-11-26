from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from EventHubApp.search.models import Category
from EventHubApp.search.models import UserProfile
from EventHubApp.search.models import Rating
from EventHubApp.search.models import User
from EventHubApp.registration.models import Userprofiledetails
from cart.cart import Cart
from django.template.context_processors import request
from EventHubApp.registration.models import States
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.core.serializers import serialize
import json

def getprofile(request):
    category_id = request.GET['category_id']
    request.session["categoryid"] = category_id
    print('catagory', category_id)
    category = Category.objects.get(category_id=category_id)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    profiles = UserProfile.objects.filter(category_id=category_id)

    profileJsons=serialize('json', list(profiles))
    profileJsons = json.dumps(profileJsons)

    # print('category', category)
    # print('profiles', profiles)
    return render(request, 'listservice.html',
                  {'profiles': profiles, 'category': category, 'list1': list1, 'stateNames': stateNames,
                   'cityNames': cityNames, 'profileJsons':profileJsons})


def getallprofile(request):
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    searchText = request.POST.get('searchText')
    print('searchText', searchText)
    categoryids = Category.objects.values_list('category_id', flat=True).filter(
        Q(category_name__contains=searchText) | Q(description__contains=searchText))
    #     filter(category_name__contains=searchText)
    #     .filter(description__contains=searchText)
    print('categoryids', list(categoryids))
    profiles = UserProfile.objects.filter(
        Q(profile_name__contains=searchText) | Q(description__contains=searchText) | Q(category_id__in=categoryids))
    #     filter(profile_name__contains=searchText).filter(description__contains=searchText).filter(category_id__in=categoryids)
    print('profiles', profiles)
    category = {
        'category_name': 'Services'
    }
    profileJsons = serialize('json', list(profiles))
    profileJsons = json.dumps(profileJsons)
    return render(request, 'listservice.html',
                  {'profiles': profiles, 'category': category, 'list1': list1, 'stateNames': stateNames,
                   'cityNames': cityNames, 'profileJsons':profileJsons})


def getdetail(request):
    profile_id = request.GET['profile_id']
    print('profile_id', profile_id)
    #     category = Category.objects.get(category_id = category_id)
    profile = UserProfile.objects.get(profile_id=profile_id)
    profile_detail = Userprofiledetails.objects.get(profile_id=profile_id)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    print('profile_detail', profile_detail.type)
    print('profile', profile)
    # range1 = range(1,6)
    range1 = (profile.pic1, profile.pic2, profile.pic3, profile.pic4, profile.pic5)
    return render(request, 'viewdetail.html',
                  {'range': range1, 'profile': profile, 'profileDetails': profile_detail, 'list1': list1,
                   'stateNames': stateNames, 'cityNames': cityNames})


def add_to_cart(request, product_id, quantity=1):
    if "userid" in request.session:
        userid = request.session["userid"]
    product = UserProfile.objects.get(profile_id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)
    list1 = Category.objects.all()
    return render(request, 'cart.html', dict(cart=Cart(request)))


def remove_from_cart(request, product_id):
    product = UserProfile.objects.get(profile_id=product_id)
    cart = Cart(request)
    cart.remove(product)
    list1 = Category.objects.all()
    return render(request, 'cart.html', dict(cart=Cart(request)))


def get_cart(request):
    return render('cart.html', dict(cart=Cart(request)))


def getprofileonprice(request):
    if "categoryid" in request.session:
        category_id = request.session["categoryid"]
    category = Category.objects.get(category_id=category_id)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    max_price = 100
    #     request.GET['max']
    min_price = 0
    #     request.GET['min']
    profiles = UserProfile.objects.filter(category_id=category_id).filter(price__range=(min_price, max_price))
    return render(request, 'listservice.html',
                  {'profiles': profiles, 'category': category, 'list1': list1, 'stateNames': stateNames,
                   'cityNames': cityNames})


def getprofileonrating(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id=category_id)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    min_rating = request.GET['min_rating']
    max_rating = request.GET['max_rating']
    profile_ids = Rating.objects.values_list('profile_id', flat=True).filter(rating__range=(min_rating, max_rating))
    profiles = UserProfile.objects.filter(category_id=category_id).filter(profile_id=set(profile_ids))
    return render(request, 'listservice.html',
                  {'profiles': profiles, 'category': category, 'list1': list1, 'stateNames': stateNames,
                   'cityNames': cityNames})


def getprofileonstate(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id=category_id)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    state = request.GET['state']
    user_id = User.objects.values_list('user_id', flat=True).filter(state=state)
    profiles = UserProfile.objects.filter(category_id=category_id).filter(user_id=set(user_id))
    return render(request, 'listservice.html',
                  {'profiles': profiles, 'category': category, 'list1': list1, 'stateNames': stateNames,
                   'cityNames': cityNames})


def getprofileonicity(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id=category_id)
    list1 = Category.objects.all()
    stateNames = States.objects.order_by().values('city_state').distinct()
    cityNames = States.objects.order_by().values('city_name').distinct()
    city = request.GET['city']
    user_id = User.objects.values_list('user_id', flat=True).filter(city=city)
    profiles = UserProfile.objects.filter(category_id=category_id).filter(user_id=set(user_id))
    return render(request, 'listservice.html',
                  {'profiles': profiles, 'category': category, 'list1': list1, 'stateNames': stateNames,
                   'cityNames': cityNames})


# def getprofileonname(request):


