
"""EventHubApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from EventHubApp.SignUp import views as core_views
from django.contrib.auth import views as auth_views
from EventHubApp.events import views as event_views
from EventHubApp.search import views as search_views
from EventHubApp.registration import views as registration_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
#     url(r'/', core_views.getData, name='getData'),
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', core_views.test, name='test'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^getdata/$', core_views.getData, name='getData'),
    url(r'^home/$', core_views.home, name='home'),
    #url(r'florist/$', event_views.florist, name='florist'),
    #url(r'florist1/$', event_views.florist1, name='florist1'),
    url(r'getprofile/$', search_views.getprofile, name='getprofile'),
    url(r'getdetail/$', search_views.getdetail, name='getdetail'),
    url(r'addtocart/(?P<product_id>[0-9]+)$', search_views.add_to_cart, name='addtocart'),
    url(r'deletefromcart/(?P<product_id>[0-9]+)$', search_views.remove_from_cart, name='deletefromcart'),
    url(r'getallprofile/$', search_views.getallprofile, name='getallprofile'),
    url(r'getprofileonprice/$', search_views.getprofileonprice, name='getprofileonprice'),
    url(r'rating/$', auth_views.login, {'template_name': 'rating.html'}, name='rating'),
    #url(r'register/$', event_views.register, name='register'),
    #url(r'getForm/$', event_views.getForm, name='getForm'),
    #url(r'registerServiceDetails/$', event_views.registerServiceDetails, name='registerServiceDetails'),
    #url(r'getServiceDetails/$', event_views.getServiceDetails, name='getServiceDetails'),
    #url(r'saveUserProfile/$', event_views.saveUserProfile, name='saveUserProfile'),
    url(r'registerServiceDetails/$', registration_views.registerServiceDetails, name='registerServiceDetails'),
    url(r'saveUserProfile/$', registration_views.saveUserProfile, name='saveUserProfile'),
    url(r'contact/$', event_views.contact, name='contact'),
    url(r'contactUs/$', event_views.contactUs, name='contactUs'),
    url(r'aboutUs/$', event_views.aboutUs, name='aboutUs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', event_views.signup, name='signup'),
    url(r'^signin/$', event_views.signin, name='signin'),
    url(r'^signupSubmit/$', event_views.signupSubmit, name='signupSubmit'),
    url(r'^account/$', event_views.account, name='account'),
    url(r'^modifyServiceUserProfile/$', event_views.modifyServiceUserProfile, name='modifyServiceUserProfile'),
    url(r'^updateUserProfileDetails/$', event_views.updateUserProfileDetails, name='updateUserProfileDetails'),
    url(r'^modifyRegularUserProfile/$', event_views.modifyRegularUserProfile, name='modifyRegularUserProfile'),
]

