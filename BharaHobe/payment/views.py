from django.shortcuts import render, redirect
from .forms import paymentForm
from .models import PaymentModel

def make_payment(request):
    if request.method == 'POST':
        form = paymentForm(request.POST)
        if form.is_valid():
            f_order_id = form.cleaned_data['f_order_id']
            f_amount = form.cleaned_data['f_amount']
            f_isSuccess = form.cleaned_data['f_isSuccess']
            payment = PaymentModel.objects.create(m_order_id=f_order_id, m_amount=f_amount, m_isSuccess=f_isSuccess)
            return render(request, 'payment_success.html', {'payment': payment})
    else:
        form = paymentForm()

    return render(request, 'make_payment.html', {'form': form})
