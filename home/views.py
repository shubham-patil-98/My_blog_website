
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    content={
        "variable":"this is shubham",
        "variable2":"this is soham",
    }
    return render(request,"index.html",content)

def about(request):
     return render(request,"about.html")
    # return HttpResponse("heya welcome to the about page")

def services(request):
    # return HttpResponse("heya welcome to the service page")
     return render(request,"services.html")

def contact(request):
    # return HttpResponse("heya wanna contact us?")
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        password=request.POST.get('Password')
        desc=request.POST.get('Reason')
        contact=Contact.objects.create(name=name,email=email,password=password,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
    return render(request,"contact.html")