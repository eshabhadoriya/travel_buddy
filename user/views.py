from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from user.models import register
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.core.mail import EmailMessage
# Create your views here.

def index(request):
    return render(request,'index.html')
def user_Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.info(request,"login successful")
            return redirect ('index')
        else:
            messages.error(request,"username or password isnt matching")
            return redirect('user_Login')
    else:
        return render(request,'login.html')
    
def Register(request):
    if request.method=="POST":
        first_name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')


       
        
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already Registered')
                return redirect('Register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
                user.save()
                messages.success(request,'User Successfully Created')
                # email_subject='User registered'
                # email_body='heyyyyy'
                # email=EmailMessage(
                #     'email_subject',
                #     'Registration successful',
                #     'bhadoriyaesha290@gmail.com',
                #     ['eshabhadoriya08@gmail.com']
                #  )
                # email.send(fail_silently=False)
                return redirect('user_Login')
        else:
            messages.error(request,'Incorrect Password')
            return redirect('Register')
    else:
        return render(request,'register.html')
   
                                                
    
def user_Logout(request):
    auth.logout(request)
    return redirect('index')
