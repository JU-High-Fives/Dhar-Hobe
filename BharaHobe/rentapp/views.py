from django.shortcuts import render

def home(request):
    return render(request,'rentapp/home.html')

def admin_page(request):
    """
    Go the the admin panel
    """
    # Retrieve all delivery requests from the database
    
    return render(request, "rentapp/admin_page.html")