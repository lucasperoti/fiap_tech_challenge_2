from core.usecases.order_usecase import OrderUseCase
from infrastructure.database.django_order_gateway import DjangoOrderGateway
from infrastructure.database.django_customer_gateway import DjangoCustomerGateway
from infrastructure.database.django_product_gateway import DjangoProductGateway

class OrderController:
    def __init__(self):
        self.order_usecase = OrderUseCase(
            order_gateway=DjangoOrderGateway(),
            customer_gateway=DjangoCustomerGateway(),
            product_gateway=DjangoProductGateway(),
        )

    def checkout(self, data):
        order = self.order_usecase.create_order(data)
        return order

    def update_status(self, order_id, new_status):
        self.order_usecase.update_order_status(order_id, new_status)

    def list_orders(self):
        return self.order_usecase.list_orders()

    def payment_status(self, order_id):
        return self.order_usecase.get_order_payment_status(order_id)

    def payment_webhook(self, data):
        self.order_usecase.handle_payment_webhook(data)