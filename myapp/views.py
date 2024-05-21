from django.shortcuts import render
from django.conf import urls
from .models import details
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get('name',False)
        email=request.POST.get('email',False)
        subject=request.POST.get('subject',False)
        message=request.POST.get('message',False)
        k = details(name= name, email= email,subject=subject,message=message )
        k.save()
    post =details.objects.all()
    
    return render(request,'home.html',{'post':post})
def login(request):
    
    
    
    return render(request,"login.html")
