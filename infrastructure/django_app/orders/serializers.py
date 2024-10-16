from rest_framework import serializers
from infrastructure.django_app.products.serializers import ProductOutputSerializer
from infrastructure.django_app.customers.serializers import CustomerInputSerializer, CustomerOutputSerializer

class OrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

class OrderInputSerializer(serializers.Serializer):
    customer = CustomerInputSerializer(allow_null=True, required=False)
    items = OrderItemInputSerializer(many=True)

class OrderItemOutputSerializer(serializers.Serializer):
    product = ProductOutputSerializer()
    quantity = serializers.IntegerField()

class OrderOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer = CustomerOutputSerializer(allow_null=True)
    items = OrderItemOutputSerializer(many=True)
    status = serializers.CharField()
    payment_status = serializers.CharField()
    created_at = serializers.DateTimeField()

class OrderStatusUpdateSerializer(serializers.Serializer):
    status = serializers.CharField()