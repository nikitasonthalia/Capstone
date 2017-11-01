from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.shortcuts import render_to_response
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
#from .gmaps import gMapfun
#from .paint import paintDraw
import importlib.util
import sys
from .models import *

categoryName = Category.objects.order_by("category_name")

#def index(request):
#    return HttpResponse("Hello Amruta. You're at the polls index.")

# def index(request):
#     template = loader.get_template('events/home.html')
#     context = {
#     }
#     return HttpResponse(template.render(context, request))

# Displays home.html
def home(request):
    template = loader.get_template('events/home.html')
    #categoryName = Category.objects.order_by("category_name")
    context = {

    }
    #userName = User.objects.filter(username='Amruta')
    #return HttpResponse(template.render(context, request))
    return render(request, 'events/home.html', {'categoryName': categoryName})

# Displays florist.html
def florist(request):
    template = loader.get_template('events/florist.html')
    context = {

    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'events/florist.html', {'categoryName': categoryName})


# Displays florist1.html
def florist1(request):
    template = loader.get_template('events/florist1.html')
    context = {

    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'events/florist1.html', {'categoryName': categoryName})