from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Core/index.html')

def login(request):
    return render(request, 'Core/login.html')

def register(request):
    return render(request, 'Core/register.html')