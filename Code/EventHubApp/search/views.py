from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from EventHubApp.search.models import Category
from EventHubApp.search.models import UserProfile
from EventHubApp.search.models import Rating
from EventHubApp.search.models import User
from cart.cart import Cart
from django.template.context_processors import request

def getprofile(request):
    category_id = request.GET['category_id']
    print('catagory',category_id)
    category = Category.objects.get(category_id = category_id)
    profiles = UserProfile.objects.filter(category_id = category_id )
    print('category',category)
    print('profiles',profiles)
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category})

def getdetail(request):
    profile_id = request.GET['profile_id']
    print('profile_id',profile_id)
#     category = Category.objects.get(category_id = category_id)
    profile = UserProfile.objects.get(profile_id = profile_id )
#     print('category',category)
    print('profile',profile)
    range1 = range(1,6)
    return render(request, 'viewdetail.html', {'range' : range1 , 'profile' : profile})

def add_to_cart(request, product_id, quantity=1):
    product = UserProfile.objects.get(profile_id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)
    return render(request, 'cart.html', dict(cart=Cart(request)))

def remove_from_cart(request, product_id):
    product = UserProfile.objects.get(profile_id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return render(request, 'cart.html', dict(cart=Cart(request)))

def get_cart(request):
    return render('cart.html', dict(cart=Cart(request)))

def getprofileonprice(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id = category_id)
    max_price = request.GET['max']
    min_price = request.GET['min']
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(price__range=(min_price, max_price))
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category})

def getprofileonrating(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id = category_id)
    min_rating= request.GET['min_rating']
    max_rating= request.GET['max_rating']
    profile_ids=Rating.objects.values_list('profile_id', flat=True).filter(rating__range=(min_rating, max_rating))
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(profile_id=set(profile_ids))
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category})

def getprofileonstate(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id = category_id)
    state = request.GET['state']
    user_id = User.objects.values_list('user_id', flat=True).filter(state=state)
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(user_id=set(user_id))
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category})

def getprofileonicity(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(category_id = category_id)
    city = request.GET['city']
    user_id = User.objects.values_list('user_id', flat=True).filter(city=city)
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(user_id=set(user_id))
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category})
# def getprofileonname(request):
    
