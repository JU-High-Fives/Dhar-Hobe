from django.shortcuts import render, redirect
from .forms import advancePaymentForm, monthlyPaymentForm, emiPaymentForm
from .models import PaymentModel, OrderModel
from .mock_payment import MockPaymentError, MockPaymentGateway

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

    If POST request, redirects to the chosen payment form,
    else renders the payment method selection page.

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
    order = OrderModel.objects.get(pk=order_id)

    if request.method == 'POST':
        form = advancePaymentForm(request.POST)

        if form.is_valid():
            payment_method = form.cleaned_data['f_payment_method']

            if payment_method == 'credit_card':
                card_token = form.cleaned_data['f_card_token']
                payment = PaymentModel.objects.create(
                    m_order_id=order.m_order_id,
                    m_amount=form.cleaned_data['f_amount'],
                    m_isSuccess=True,
                    m_payment_method='credit_card',
                    m_notes=form.cleaned_data['f_notes'],
                    m_card_token=card_token
                )
                return render(request, 'payment_success.html', {'payment': payment})

    else:
        form = advancePaymentForm()

    return render(request, 'advance_payment_form.html', {'form': form, 'order': order})

def monthly_payment_view(request):
    """
    View for handling monthly payment form.

    If POST request, processes form data, creates PaymentModel, and renders payment success page.
    If GET request, renders the monthly payment form.

    Returns:
        HttpResponse: Rendered template for monthly payment form or payment success.
    """
    if request.method == 'POST':
        form = monthlyPaymentForm(request.POST)
        if form.is_valid():
            f_order_id = form.cleaned_data['f_order_id']
            f_amount = form.cleaned_data['f_amount']
            f_isSuccess = form.cleaned_data['f_isSuccess']
            payment = PaymentModel.objects.create(m_order_id=f_order_id, m_amount=f_amount, m_isSuccess=f_isSuccess)
            return render(request, 'payment_success.html', {'payment': payment})
    
    else:
        form = monthlyPaymentForm()

    return render(request, 'monthly_payment_form.html', {'form': form})

def emi_payment_view(request):
    """
    View for handling EMI payment form.

    If POST request, processes form data, creates PaymentModel, and renders payment success page.
    If GET request, renders the EMI payment form.

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

    Displays details of the successful payment.

    Returns:
        HttpResponse: Rendered template for payment success
    """
    latest_payment = PaymentModel.objects.filter(m_isSuccess=True).order_by('-id').first()

    return render(request, 'payment_success.html', {'latest_payment': latest_payment})

