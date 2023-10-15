from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from home.models import Contact


# Create your views here.
def index(request):
    
   # context={
       # "variable":"hey esha here"
   #}
    return render(request,'index.html')
    #return render(request,'index.html',context)
    #return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
   # return HttpResponse("this is about page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is service page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        formss=Contact.objects.create(name=name,email=email,subject=subject,desc=desc)
        formss.save()
        
        messages.info(request,'Information Saved')
            
        return redirect('index')
    else:
        return render(request,'contact.html')


# # from .forms import ContactForm
# from home.forms import ContactForm


        
   
    #     else:
    #         messages.error(request,'Incorrect Password')
    #         return redirect('Register')
    # else:
    #     return render(request,'register.html')
   
    # return render(request,'contact.html')
    # #return HttpResponse("this is contact page")