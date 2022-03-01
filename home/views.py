from django.shortcuts import render

# Create your views here.

def home_page(request):
    welcome = 'Testing'
    return render(request,'home/home.html',{'weclome':welcome})
