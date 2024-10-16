from abc import ABC, abstractmethod
from core.entities.models import Product

class ProductGateway(ABC):
    @abstractmethod
    def list_all_products(self) -> list:
        pass

    @abstractmethod
    def list_products_by_category(self, category_name: str) -> list:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def create_product(self, product_data: dict) -> Product:
        pass