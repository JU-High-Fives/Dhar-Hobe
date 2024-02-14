from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .services import EmailService, ProductService
from django.utils import timezone

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
    renter_product.is_approved = 'approved'  # Set the is_approved field to 
    renter_product.approved_at=timezone.now()
    renter_product.save()  # Save the changes
    ProductService().approve_product(renter_product)
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
    renter_product.is_approved = 'disapproved'  # Set the is_approved field to False
    renter_product.approved_at=timezone.now()
    renter_product.save()  # Save the changes
    ProductService().disapprove_product(renter_product)
    
    return HttpResponseRedirect(reverse('add_product_rqsts'))

def add_product_rqsts(request):
    """
    View function to display and handle product requests.

    If a POST request is received, it handles the action based on the request_id and action parameters.
    Otherwise, it renders the page with a list of product requests.

    Parameters:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Renders the add product requests page with a list of product requests with is_approved status pending.
    """
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        
        renter_product = RenterProduct.objects.get(id=request_id)
        ProductService().handle_action(action, renter_product)

    requests = RenterProduct.objects.filter(is_approved='pending')
    
    if not requests:
        # If there are no products available, render a message
        return HttpResponse('No add products requests for rent is available')
    context = {'requests': requests}
    return render(request, 'app_rentApproval/add_product_rqsts.html', context)

def approved_requests(request):
    """
    View function to display approved product requests.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the approved requests page with a list of approved product requests.
    """
    approved_requests = RenterProduct.objects.filter(is_approved='approved')
    context = {'approved_requests': approved_requests}
    return render(request, 'app_rentApproval/approved_requests.html', context)

def disapproved_requests(request):
    """
    View function to display disapproved product requests.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the disapproved requests page with a list of disapproved product requests.
    """
    disapproved_requests = RenterProduct.objects.filter(is_approved='disapproved')
    context = {'disapproved_requests': disapproved_requests}
    return render(request, 'app_rentApproval/disapproved_requests.html', context)

