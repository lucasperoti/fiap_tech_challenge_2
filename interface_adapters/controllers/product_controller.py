from core.usecases.product_usecase import ProductUseCase
from infrastructure.database.django_product_gateway import DjangoProductGateway

class ProductController:
    def __init__(self):
        self.product_usecase = ProductUseCase(product_gateway=DjangoProductGateway())

    def list_all_products(self):
        return self.product_usecase.list_all_products()

    def list_products_by_category(self, category_name):
        return self.product_usecase.list_products_by_category(category_name)

    def get_product_by_id(self, product_id):
        return self.product_usecase.get_product_by_id(product_id)

    def create_product(self, product_data):
        return self.product_usecase.create_product(product_data)