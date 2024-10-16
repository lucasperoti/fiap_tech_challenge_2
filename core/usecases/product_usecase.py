from interface_adapters.gateways.product_gateway import ProductGateway
from core.entities.models import Product

class ProductUseCase:
    def __init__(self, product_gateway: ProductGateway):
        self.product_gateway = product_gateway

    def list_all_products(self) -> list:
        return self.product_gateway.list_all_products()

    def list_products_by_category(self, category_name: str) -> list:
        return self.product_gateway.list_products_by_category(category_name)

    def get_product_by_id(self, product_id: int) -> Product:
        return self.product_gateway.get_product_by_id(product_id)

    def create_product(self, product_data: dict) -> Product:
        return self.product_gateway.create_product(product_data)