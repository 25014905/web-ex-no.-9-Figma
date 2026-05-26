from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def events(request):
    return render(request,'events.html')

def details(request):
    return render(request,'details.html')

def success(request):
    return render(request,'success.html')