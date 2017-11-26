from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from EventHubApp.search.models import Category
from EventHubApp.search.models import UserProfile
from EventHubApp.search.models import Rating
from EventHubApp.search.models import User
from EventHubApp.search.models import Rating
from EventHubApp.registration.models import Userprofiledetails
from cart.cart import Cart
from django.template.context_processors import request

def getprofile(request):
    category_id = request.GET['category_id']
    request.session["categoryid"] = category_id
    print('catagory',category_id)
    category = Category.objects.get(category_id = category_id)
    list1 = Category.objects.all()
    profiles = UserProfile.objects.filter(category_id = category_id )
    print('category',category)
    print('profiles',profiles)
    cart = Cart(request)
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category, 'list1' : list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def getallprofile(request):
    list1 = Category.objects.all()
    searchText = request.POST.get('searchText')
    print('searchText',searchText)
    categoryids = Category.objects.values_list('category_id', flat=True).filter(Q(category_name__contains=searchText) | Q(description__contains=searchText))
#     filter(category_name__contains=searchText)
#     .filter(description__contains=searchText)
    print('categoryids',list(categoryids))
    profiles = UserProfile.objects.filter(Q(profile_name__contains=searchText) | Q(description__contains=searchText) | Q(category_id__in=categoryids))
#     filter(profile_name__contains=searchText).filter(description__contains=searchText).filter(category_id__in=categoryids)
    print('profiles',profiles)
    category = {
        'category_name' : 'Services'
    }
    cart = Cart(request)
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category, 'list1' : list1, 'cartlength': cart.count(), 'tot': cart.summary() })


def getdetail(request):
    profile_id = request.GET['profile_id']
    print('profile_id',profile_id)
#     category = Category.objects.get(category_id = category_id)
    profile = UserProfile.objects.get(profile_id = profile_id )
    profile_detail = Userprofiledetails.objects.get(profile_id = profile_id)
    list1 = Category.objects.all()
    print('profile_detail',profile_detail.type)
    print('profile',profile)
    range1 = range(1,6)
    cart = Cart(request)
    feedback = Rating.objects.filter(profile = profile_id)
    return render(request, 'viewdetail.html', {'range' : range1 , 'profile' : profile, 'profileDetails':profile_detail, 'list1':list1, 'cartlength': cart.count(), 'tot': cart.summary(),'feedbacks':feedback })

def add_to_cart(request, product_id, quantity=1):
#     if "userid" in request.session:
#         userid = request.session["userid"]
    product = UserProfile.objects.get(profile_id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)
    cart = Cart(request)
    list1 = Category.objects.all()
    return render(request, 'cart.html', {'cart': dict(cart=Cart(request)),'list1':list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def remove_from_cart(request, product_id):
    product = UserProfile.objects.get(profile_id=product_id)
    cart = Cart(request)
    cart.remove(product)
    list1 = Category.objects.all()
    return render(request, 'cart.html', {'cart': dict(cart=Cart(request)),'list1':list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def get_cart(request):
    print('here')
    cart = Cart(request)
    list1 = Category.objects.all()
    return render(request,'cart.html', {'cart': dict(cart=Cart(request)),'list1':list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def getprofileonprice(request):
    if "categoryid" in request.session:
        category_id = request.session["categoryid"]
    category = Category.objects.get(category_id = category_id)
    list1 = Category.objects.all()
    if 'max' in request.GET and 'min' in request.GET:
        print('In GET')
        max_price = request.GET['max']
        min_price = request.GET['min']
    else: 
        max_price = request.POST['maxPrice']
        min_price = request.POST['minPrice']
        print('In POST')
    cart = Cart(request)
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(price__range=(min_price, max_price))
    
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category, 'list1': list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def getprofileonrating(request):
    if "categoryid" in request.session:
        category_id = request.session["categoryid"]
    category = Category.objects.get(category_id = category_id)
    list1 = Category.objects.all()
    cart = Cart(request)
    min_rating= request.GET['min_rating']
    max_rating= request.GET['max_rating']
    profile_ids=Rating.objects.values_list('profile_id', flat=True).filter(rating__range=(min_rating, max_rating))
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(profile_id__in=profile_ids)
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category, 'list1': list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def getprofileonstate(request):
    category_id = request.GET['category_id']
    cart = Cart(request)
    category = Category.objects.get(category_id = category_id)
    list1 = Category.objects.all()
    state = request.GET['state']
    user_id = User.objects.values_list('user_id', flat=True).filter(state=state)
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(user_id=set(user_id))
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category, 'list1': list1, 'cartlength': cart.count(), 'tot': cart.summary() })

def getprofileonicity(request):
    category_id = request.GET['category_id']
    cart = Cart(request)
    category = Category.objects.get(category_id = category_id)
    list1 = Category.objects.all()
    city = request.GET['city']
    user_id = User.objects.values_list('user_id', flat=True).filter(city=city)
    profiles = UserProfile.objects.filter(category_id = category_id ).filter(user_id=set(user_id))
    return render(request, 'listservice.html', {'profiles' : profiles, 'category' : category, 'list1': list1, 'cartlength': cart.count(), 'tot': cart.summary() })
# def getprofileonname(request):

def saverating(request, product_id):
    if "userid" in request.session:
        userid = request.session["userid"]
    feedback = request.POST.get('feedback')
    rating = request.POST.get('rating')
    print(rating)
    ratingprofile =  Rating(profile = UserProfile.objects.get(profile_id=product_id), rating = rating , description = feedback , user = User.objects.get(user_id = userid) )
    ratingprofile.save()
    cart = Cart(request)
    list1 = Category.objects.all()
    return render(request, 'rating.html', {'profile_id' : product_id, 'list1': list1, 'cartlength': cart.count(), 'tot': cart.summary() })

    

def redirectrating(request, product_id):
    cart = Cart(request)
    list1 = Category.objects.all()
    return render(request, 'rating.html', {'profile_id' : product_id, 'list1': list1, 'cartlength': cart.count(), 'tot': cart.summary() })

