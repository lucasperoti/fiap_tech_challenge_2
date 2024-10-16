from django.urls import path
from .views import (
    CheckoutView,
    UpdateOrderStatusView,
    OrderListView,
    PaymentStatusView,
    PaymentWebhookView,
)

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('<int:order_id>/update-status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('', OrderListView.as_view(), name='order_list'),
    path('<int:order_id>/payment-status/', PaymentStatusView.as_view(), name='payment_status'),
    path('payment-webhook/', PaymentWebhookView.as_view(), name='payment_webhook'),
]