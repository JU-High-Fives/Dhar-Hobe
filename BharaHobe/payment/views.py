from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            success = form.cleaned_data['success']
            payment = Payment.objects.create(order_id=order_id, amount=amount, success=success)
            return render(request, 'payment_success.html', {'payment': payment})
    else:
        form = PaymentForm()

    return render(request, 'make_payment.html', {'form': form})
