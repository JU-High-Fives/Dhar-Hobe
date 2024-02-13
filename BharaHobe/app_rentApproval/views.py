from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .services import EmailService, ProductService
# Create your views here.
def admin_page(request):
    """This function renders to the admin page from userprofile page

    """
    return render(request, 'app_rentApproval/admin_page.html')


def approve_product(request, request_id):
    """
    View function to approve a product request.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        request_id (int): The ID of the product request to be approved.
        
    Returns:
        HttpResponseRedirect: Redirects to the add product requests page.
    """
    renter_product = RenterProduct.objects.get(id=request_id)
    ProductService().approve_product(renter_product)
    renter_product.is_approved = True  # Set the is_approved field to True
    renter_product.save()  # Save the changes
    return HttpResponseRedirect(reverse('add_product_rqsts'))

def disapprove_product(request, request_id):
    """
    View function to disapprove a product request.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        request_id (int): The ID of the product request to be disapproved.
        
    Returns:
        HttpResponseRedirect: Redirects to the add product requests page.
    """
    renter_product = RenterProduct.objects.get(id=request_id)
    ProductService().disapprove_product(renter_product)
    renter_product.is_approved = False  # Set the is_approved field to False
    renter_product.save()  # Save the changes
    return HttpResponseRedirect(reverse('add_product_rqsts'))

def add_product_rqsts(request):
    """
    View function to display and handle product requests.

    If a POST request is received, it handles the action based on the request_id and action parameters.
    Otherwise, it renders the page with a list of product requests.

    Parameters:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the add product requests page with a list of product requests.
    """
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        
        renter_product = RenterProduct.objects.get(id=request_id)
        ProductService().handle_action(action, renter_product)

    requests = RenterProduct.objects.all()
    if not requests:
        # If there are no products available, render a message
        return HttpResponse('No products available for rent.')
    context = {'requests': requests}
    return render(request, 'app_rentApproval/add_product_rqsts.html', context)
