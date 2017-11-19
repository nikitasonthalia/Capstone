
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
from django.conf.urls import url
from django.contrib import admin
from EventHubApp.SignUp import views as core_views
from django.contrib.auth import views as auth_views
from EventHubApp.events import views as event_views
from EventHubApp.search import views as search_views

urlpatterns = [
#     url(r'/', core_views.getData, name='getData'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^getdata/$', core_views.getData, name='getData'),
    url(r'^home/$', event_views.home, name='home'),
    url(r'florist/$', event_views.florist, name='florist'),
    url(r'florist1/$', event_views.florist1, name='florist1'),
    url(r'getprofile/$', search_views.getprofile, name='getprofile'),
    url(r'getdetail/$', search_views.getdetail, name='getdetail'),
    url(r'addtocart/(?P<product_id>[0-9]+)$', search_views.add_to_cart, name='addtocart'),
    url(r'deletefromcart/(?P<product_id>[0-9]+)$', search_views.remove_from_cart, name='deletefromcart'),
    url(r'getallprofile/$', search_views.getallprofile, name='getallprofile'),
    url(r'getprofileonprice/$', search_views.getprofileonprice, name='getprofileonprice'),
    url(r'rating/$', auth_views.login, {'template_name': 'rating.html'}, name='rating'),

    
    
]
