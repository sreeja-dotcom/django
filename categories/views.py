from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.
def index(request):
    #return HttpResponse("<h1>Welcome to django</h1>")
    x = Products.objects.all()
    return render(request,'index.html',{'x':x})
def about(request):
    return HttpResponse("<h1>About Page</h1>")
def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")