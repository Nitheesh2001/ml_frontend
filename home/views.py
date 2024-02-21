from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from  .models import Details

# Create your views here.


def index(request):
    context={
        "variable1":"this is send",
         "variable2":"new one"
    }
    # messages.success(request, "this is a test message")

    return render(request,'index.html',context)
    # return HttpResponse("this is home page")

def details(request):
     if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        new_details = Details(name=name, email=email,subject=subject)
        new_details.save()
        messages.success(request, "Your Message Had Been Send!")

     return render(request,'details.html')

def cadidate(request):
    return render(request,'cadidate.html')