from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
#from .gmaps import gMapfun
#from .paint import paintDraw
import importlib.util
import sys


#def index(request):
#    return HttpResponse("Hello Amruta. You're at the polls index.")

def index(request):
    template = loader.get_template('events/home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

# Displays home.html
def home(request):
    template = loader.get_template('events/home.html')
    context = {

    }
    return HttpResponse(template.render(context,request))
