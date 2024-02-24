from django.shortcuts import render
from .models import Product    

def home(request):
    # Add your view logic here
    return render(request, 'home.html')
