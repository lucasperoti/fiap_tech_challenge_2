from core.usecases.customer_usecase import CustomerUseCase
from infrastructure.database.django_customer_gateway import DjangoCustomerGateway

class CustomerController:
    def __init__(self):
        self.customer_usecase = CustomerUseCase(customer_gateway=DjangoCustomerGateway())

    def list_customers(self):
        return self.customer_usecase.list_customers()

    def get_customer_by_id(self, customer_id):
        return self.customer_usecase.get_customer_by_id(customer_id)

    def create_customer(self, customer_data):
        return self.customer_usecase.create_customer(customer_data)