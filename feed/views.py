
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def contact_view(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
     
    return render(request,'contact.html')
