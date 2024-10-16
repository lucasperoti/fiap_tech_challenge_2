from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from interface_adapters.controllers.product_controller import ProductController
from .serializers import ProductInputSerializer, ProductOutputSerializer, CategoryInputSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductListView(APIView):
    @swagger_auto_schema(
        operation_description="Lista todos os produtos ou filtra por categoria.",
        manual_parameters=[
            openapi.Parameter('category', openapi.IN_QUERY, description="Nome da categoria", type=openapi.TYPE_STRING)
        ],
        responses={200: ProductOutputSerializer(many=True)}
    )
    def get(self, request):
        controller = ProductController()
        category_name = request.query_params.get('category')
        if category_name:
            products = controller.list_products_by_category(category_name)
        else:
            products = controller.list_all_products()
        serializer = ProductOutputSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Cria um novo produto.",
        request_body=ProductInputSerializer,
        responses={201: ProductOutputSerializer},
        examples={
            'application/json': {
                'name': 'Hambúrguer Especial',
                'description': 'Delicioso hambúrguer com ingredientes selecionados.',
                'price': '19.90',
                'category': {'name': 'Lanche'},
                'image': None
            }
        }
    )
    def post(self, request):
        controller = ProductController()
        serializer = ProductInputSerializer(data=request.data)
        if serializer.is_valid():
            product = controller.create_product(serializer.validated_data)
            output_serializer = ProductOutputSerializer(product)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Obtém detalhes de um produto pelo ID.",
        responses={200: ProductOutputSerializer}
    )
    def get(self, request, product_id):
        controller = ProductController()
        product = controller.get_product_by_id(product_id)
        serializer = ProductOutputSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
