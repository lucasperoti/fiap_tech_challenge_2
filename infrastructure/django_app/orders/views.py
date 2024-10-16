from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from interface_adapters.controllers.order_controller import OrderController
from .serializers import (
    OrderInputSerializer,
    OrderOutputSerializer,
    OrderStatusUpdateSerializer
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CheckoutView(APIView):
    @swagger_auto_schema(
        operation_description="Realiza o checkout de um pedido.",
        request_body=OrderInputSerializer,
        responses={201: OrderOutputSerializer},
        examples={
            'application/json': {
                'customer': {
                    'cpf': '123.456.789-00',
                    'name': 'Maria Oliveira',
                    'email': 'maria.oliveira@example.com'
                },
                'items': [
                    {'product_id': 1, 'quantity': 2},
                    {'product_id': 3, 'quantity': 1}
                ]
            }
        }
    )
    def post(self, request):
        controller = OrderController()
        serializer = OrderInputSerializer(data=request.data)
        if serializer.is_valid():
            order = controller.checkout(serializer.validated_data)
            output_serializer = OrderOutputSerializer(order)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateOrderStatusView(APIView):
    @swagger_auto_schema(
        operation_description="Atualiza o status de um pedido.",
        request_body=OrderStatusUpdateSerializer,
        responses={200: 'Status do pedido atualizado com sucesso'}
    )
    def patch(self, request, order_id):
        controller = OrderController()
        serializer = OrderStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            new_status = serializer.validated_data.get('status')
            controller.update_status(order_id, new_status)
            return Response({'message': 'Status do pedido atualizado com sucesso'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListView(APIView):
    @swagger_auto_schema(
        operation_description="Lista todos os pedidos.",
        responses={200: OrderOutputSerializer(many=True)}
    )
    def get(self, request):
        controller = OrderController()
        orders = controller.list_orders()
        serializer = OrderOutputSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PaymentStatusView(APIView):
    @swagger_auto_schema(
        operation_description="Consulta o status de pagamento de um pedido.",
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'order_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'payment_status': openapi.Schema(type=openapi.TYPE_STRING)
            },
            example={'order_id': 1, 'payment_status': 'Aprovado'}
        )}
    )
    def get(self, request, order_id):
        controller = OrderController()
        payment_status = controller.payment_status(order_id)
        return Response({'order_id': order_id, 'payment_status': payment_status}, status=status.HTTP_200_OK)

class PaymentWebhookView(APIView):
    @swagger_auto_schema(
        operation_description="Webhook para receber notificações de pagamento de provedores externos.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'order_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID do pedido'),
                'payment_status': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Status do pagamento',
                    enum=['Aprovado', 'Recusado']
                ),
            },
            required=['order_id', 'payment_status'],
            example={
                'order_id': 1,
                'payment_status': 'Aprovado'
            }
        ),
        responses={200: openapi.Response(description='Webhook processado com sucesso')}
    )
    def post(self, request):
        controller = OrderController()
        controller.payment_webhook(request.data)
        return Response({'message': 'Webhook processado com sucesso'}, status=status.HTTP_200_OK)