from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'form_user','class':'my_form-control'}),required = True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'form_email','class':'my_form-control'}),required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'form_password','class':'my_form-control'}),required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'form_password','class':'my_form-control'}),required = True)

    # password cannot be formed using Meta
    #https://stackoverflow.com/questions/26850164/django-placeholders
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
       
   
      