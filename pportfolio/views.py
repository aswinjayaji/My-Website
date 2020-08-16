from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# UserCreation form is a build in form
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.core.mail import send_mail


def login_view(request):
    form = CustomUserForm()                           # 
    if request.method == 'POST':                      # for both for form and login
        usern=request.POST.get('usern')
        passw=request.POST.get('passw')   
        usera = authenticate(request, username=usern,password=passw)      
        form = CustomUserForm(request.POST)                            # This is for 
        if form.is_valid():                                            # form all that
            form.save()                                                # is hashed
            user = form.cleaned_data.get('username')                   #
            messages.success(request,'Account was created for '+ user) #
            return redirect('login')                                   #
        elif usera is not None:
             login(request,usera )    
             return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect ')
         
    context = {                                             # this s needed 
        'form': form                                        # only for form
    }                                                       # i.e post
    return render(request, "login/login.html", context)

def register_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form

    }
    return render(request, "login/register.html", context)
def home_view(request):                #contact form
    if request.method == 'POST':
        cont_name = request.POST.get('name')
        cont_messsege = request.POST.get('message')
        cont_email = request.POST.get('email')
        send_mail(
            cont_name,        #subject
            'From:'+cont_email+'\n'+cont_messsege,    #message
            'aswinjayajimdaj@gmail.com',       #email address of sender
            ['aswinjayajicet@gmail.com'], #email address of reciever
            fail_silently=False,                            #youcan put more email by comma   
        )
        context={
            'name':cont_name
        }
        return render(request,"index.html",context)
    else:
        return render(request,"index.html") 
    #https://www.youtube.com/watch?v=xNqnHmXIuzU for trail for forms