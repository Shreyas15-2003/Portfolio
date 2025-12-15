from django.shortcuts import render,redirect
from .models import details

# Create your views here.

def portfolio(request):
    return render(request,'portfolio.html')

def userdetails(request):
    if request.method=='POST':
        queries=details()
        queries.name=request.POST['name']
        queries.contact_no=request.POST['number']
        queries.email=request.POST['email']
        queries.message=request.POST['description']
        queries.save()
    return redirect('portfolio')