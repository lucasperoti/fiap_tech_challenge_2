from interface_adapters.gateways.customer_gateway import CustomerGateway
from core.entities.models import Customer

class CustomerUseCase:
    def __init__(self, customer_gateway: CustomerGateway):
        self.customer_gateway = customer_gateway

    def list_customers(self) -> list:
        return self.customer_gateway.list_customers()

    def get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_gateway.get_customer_by_id(customer_id)

    def create_customer(self, customer_data: dict) -> Customer:
        return self.customer_gateway.create_customer(customer_data)