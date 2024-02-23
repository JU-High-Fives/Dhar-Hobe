from django.shortcuts import render, redirect, get_object_or_404
from .forms import advancePaymentForm, monthlyPaymentForm, emiPaymentForm
from .models import PaymentModel, OrderModel
from django.http import HttpResponseBadRequest

def show_orders(request):
    """
    Shows all the orders in card with a payment button

    Args:
        request (HttpRequest): The HTTP request object
    
    Returns:
        HttpResponse: Rendered template for order list showing

    """
    orders = OrderModel.objects.all()
    return render(request, 'show_orders.html', {'orders': orders})

def select_payment_method_view(request, order_id):
    """
    View for selecting payment method.

    Args:
        order_id (int): The ID of the selected order.

    Returns:
        HttpResponse: Rendered template for payment method selection or redirect to payment form.
    """
    order = OrderModel.objects.get(pk=order_id)
    
    if request.method == 'POST':
        selected_payment_method = request.POST.get('payment_method')
        if selected_payment_method == 'advance':
            return redirect('advance_payment_form', order_id=order_id)
        elif selected_payment_method == 'monthly':
            return redirect('monthly_payment_form', order_id=order_id)
        elif selected_payment_method == 'emi':
            return redirect('emi_payment_form', order_id=order_id)
    return render(request, 'payment_method_selection.html', {'order': order})

def advance_payment_view(request, order_id):
    """
    View for processing advance payments.

    Args:
        request (HttpRequest): The HTTP request.
        order_id (int): The ID of the order for which the payment is being made.

    Returns:
        HttpResponse: Rendered HTML response.

    Raises:
        None

    """
    order = get_object_or_404(OrderModel, pk=order_id)
    
    if request.method == 'POST':
        form = advancePaymentForm(request.POST)

        if form.is_valid():
            payment_method = form.cleaned_data['f_payment_method']

            if payment_method == 'credit_card':
                card_token = form.cleaned_data['f_card_token']
                amount_to_pay = form.cleaned_data['f_amount']
                existing_payment = PaymentModel.objects.filter(m_order_id=order.m_order_id).first()

                if existing_payment:
                    return HttpResponseBadRequest("Payment for this order has already been made.")

                if amount_to_pay == order.m_total_amount:
                    payment = PaymentModel.objects.create(
                        m_order_id=order.m_order_id,
                        m_amount=amount_to_pay,
                        m_isSuccess=True,
                        m_payment_method='credit_card',
                        m_notes=form.cleaned_data['f_notes'],
                        m_card_token=card_token
                    )
                    return render(request, 'payment_success.html', {'payment': payment})
                else:
                    return HttpResponseBadRequest("Please pay the exact amount.")
    else:
        form = advancePaymentForm()
    return render(request, 'advance_payment_form.html', {'form': form, 'order': order})

def monthly_payment_view(request, order_id):
    """
    View for processing monthly payments.

    Args:
        request (HttpRequest): The HTTP request.
        order_id (int): The ID of the order for which the payment is being made.

    Returns:
        HttpResponse: Rendered HTML response.

    Raises:
        None

    """
    order = get_object_or_404(OrderModel, pk=order_id)
    
    if request.method == 'POST':
        form = monthlyPaymentForm(request.POST)

        if form.is_valid():
            # Extract relevant data from the form
            total_amount = form.cleaned_data['total_amount']
            is_success = form.cleaned_data['f_is_success']

            # Get the amounts for each month
            monthly_amounts = [form.cleaned_data[f'f_month_{i}'] for i in range(1, 7)]

            # Placeholder: Add your logic here to handle the monthly payment data
            # For example, you might want to store the data in a database, trigger payments, etc.

            # Example: Print the data for demonstration purposes
            print(f"Order ID: {order_id}")
            print(f"Total Amount: {total_amount}")
            print(f"Success: {is_success}")
            print("Monthly Amounts:")
            for i, amount in enumerate(monthly_amounts, start=1):
                print(f"Month {i}: {amount}")

            # Placeholder: Add your actual logic here

            # Redirect to a success page or return a response
            return render(request, 'success_template.html')

    else:
        # If it's a GET request, create a new form
        form = monthlyPaymentForm()

    return render(request, 'monthly_payment_form.html', {'form': form, 'order': order})

def emi_payment_view(request):
    """
    View for handling EMI payment form.

    Returns:
        HttpResponse: Rendered template for EMI payment form or payment success.
    """
    
    if request.method == 'POST':
        form = emiPaymentForm(request.POST)
        
        if form.is_valid():
            f_order_id = form.cleaned_data['f_order_id']
            f_amount = form.cleaned_data['f_amount']
            f_isSuccess = form.cleaned_data['f_isSuccess']
            payment = PaymentModel.objects.create(m_order_id=f_order_id, m_amount=f_amount, m_isSuccess=f_isSuccess)
            return render(request, 'payment_success.html', {'payment': payment})
    else:
        form = emiPaymentForm()

    return render(request, 'emi_payment_form.html', {'form': form})

def payment_success(request):
    """This function renders the payment success page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: Rendered template for payment success
    """
    latest_payment = PaymentModel.objects.filter(m_isSuccess=True).order_by('-id').first()
    return render(request, 'payment_success.html', {'latest_payment': latest_payment})

