from abc import ABC, abstractmethod
from core.entities.models import Customer

class CustomerGateway(ABC):
    @abstractmethod
    def list_customers(self) -> list:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def create_customer(self, customer_data: dict) -> Customer:
        pass

    @abstractmethod
    def get_or_create_customer(self, customer_data: dict) -> Customer:
        pass