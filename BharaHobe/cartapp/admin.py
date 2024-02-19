from django.contrib import admin
from .models import PaymentModel

@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    search_fields = ['m_order_id']  # Specify the field(s) you want to enable search on
