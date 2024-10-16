from django.db import models
from infrastructure.django_app.customers.models import Customer
from infrastructure.django_app.products.models import Product

class OrderStatus(models.TextChoices):
    RECEIVED = 'Recebido', 'Recebido'
    PREPARING = 'Em preparação', 'Em preparação'
    READY = 'Pronto', 'Pronto'
    FINALIZED = 'Finalizado', 'Finalizado'

class PaymentStatus(models.TextChoices):
    APPROVED = 'Aprovado', 'Aprovado'
    DECLINED = 'Recusado', 'Recusado'
    PENDING = 'Pendente', 'Pendente'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.RECEIVED)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
