from django import forms
from django.forms import ModelForm
from .models import ServiceProviders

class ServiceProvidersForm(forms.ModelForm):

    class Meta:
        model = ServiceProviders
        widgets = {'passwd': forms.PasswordInput()}
        #fields = ('title','inputFname','inputLname','emailId','passwd','pic','stadd1','stadd2','city','state','zip','phone','serviceType','serviceDesc',)
        fields = '__all__'


