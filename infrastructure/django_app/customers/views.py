from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from interface_adapters.controllers.customer_controller import CustomerController
from .serializers import CustomerInputSerializer, CustomerOutputSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CustomerListView(APIView):
    @swagger_auto_schema(
        operation_description="Lista todos os clientes.",
        responses={200: CustomerOutputSerializer(many=True)}
    )
    def get(self, request):
        controller = CustomerController()
        customers = controller.list_customers()
        serializer = CustomerOutputSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Cria um novo cliente.",
        request_body=CustomerInputSerializer,
        responses={201: CustomerOutputSerializer},
        examples={
            'application/json': {
                'cpf': '123.456.789-00',
                'name': 'João da Silva',
                'email': 'joao.silva@example.com'
            }
        }
    )
    def post(self, request):
        controller = CustomerController()
        serializer = CustomerInputSerializer(data=request.data)
        if serializer.is_valid():
            customer = controller.create_customer(serializer.validated_data)
            output_serializer = CustomerOutputSerializer(customer)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Obtém detalhes de um cliente pelo ID.",
        responses={200: CustomerOutputSerializer}
    )
    def get(self, request, customer_id):
        controller = CustomerController()
        customer = controller.get_customer_by_id(customer_id)
        serializer = CustomerOutputSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
