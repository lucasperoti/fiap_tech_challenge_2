from abc import ABC, abstractmethod
from core.entities.models import Order

class OrderGateway(ABC):
    @abstractmethod
    def save_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def update_order_status(self, order_id: int, new_status: str):
        pass

    @abstractmethod
    def list_orders(self) -> list:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def update_payment_status(self, order_id: int, payment_status: str):
        pass