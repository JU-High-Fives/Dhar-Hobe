from django.shortcuts import render, redirect
from .forms import advancePaymentForm, monthlyPaymentForm, emiPaymentForm
from .models import PaymentModel

def select_payment_method_view(request):
    if request.method == 'POST':
        selected_payment_method = request.POST.get('payment_method')
        if selected_payment_method == 'advance':
            return redirect('advance_payment_form')
        elif selected_payment_method == 'monthly':
            return redirect('monthly_payment_form')
        elif selected_payment_method == 'emi':
            return redirect('emi_payment_form')

    return render(request, 'payment_method_selection.html')

def advance_payment_view(request):
    if request.method == 'POST':
        form = advancePaymentForm(request.POST)
        if form.is_valid():
            f_order_id = form.cleaned_data['f_order_id']
            f_amount = form.cleaned_data['f_amount']
            f_isSuccess = form.cleaned_data['f_isSuccess']
            payment = PaymentModel.objects.create(m_order_id=f_order_id, m_amount=f_amount, m_isSuccess=f_isSuccess)
            return render(request, 'payment_success.html', {'payment': payment})
    else:
        form = advancePaymentForm()

    return render(request, 'advance_payment_form.html', {'form': form})

def monthly_payment_view(request):
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

