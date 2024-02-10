from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def admin_page(request):
    """This function renders to the admin page from userprofile page

    """
    return render(request, 'app_rentApproval/admin_page.html')

def add_product_rqsts(request):
    """This function renders to the page where a list of add product request by renter is shown

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object sent by the client.

    Returns:
    --------
    HttpResponse
        A response object containing the rendered HTML page showing the list of product requests.
    """
    
    requests=RenterProduct.objects.all()
    if not requests:
        # If there are no products available, render a message
        return HttpResponse('No products available for rent.')
    context = {'requests':requests}
    return render(request,'app_rentApproval/add_product_rqsts.html',context)
