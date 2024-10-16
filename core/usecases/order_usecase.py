from core.entities.models import Order, OrderItem, OrderStatus
from interface_adapters.gateways.order_gateway import OrderGateway
from interface_adapters.gateways.customer_gateway import CustomerGateway
from interface_adapters.gateways.product_gateway import ProductGateway

class OrderUseCase:
    def __init__(self, order_gateway: OrderGateway, customer_gateway: CustomerGateway, product_gateway: ProductGateway):
        self.order_gateway = order_gateway
        self.customer_gateway = customer_gateway
        self.product_gateway = product_gateway

    def create_order(self, data: dict) -> Order:
        customer_data = data.get('customer')
        items_data = data.get('items')

        customer = None
        if customer_data:
            customer = self.customer_gateway.get_or_create_customer(customer_data)

        items = []
        for item_data in items_data:
            product = self.product_gateway.get_product_by_id(item_data['product_id'])
            quantity = item_data.get('quantity', 1)
            items.append(OrderItem(product=product, quantity=quantity))

        order = Order(customer=customer, items=items)
        saved_order = self.order_gateway.save_order(order)
        return saved_order

    def update_order_status(self, order_id: int, new_status: str):
        self.order_gateway.update_order_status(order_id, new_status)

    def list_orders(self) -> list:
        return self.order_gateway.list_orders()

    def get_order_payment_status(self, order_id: int) -> str:
        order = self.order_gateway.get_order_by_id(order_id)
        return order.payment_status

    def handle_payment_webhook(self, data: dict):
        payment_status = data.get('payment_status')
        order_id = data.get('order_id')

        if not payment_status or not order_id:
            return

        self.order_gateway.update_payment_status(order_id, payment_status)
        if payment_status == 'Aprovado':
            self.order_gateway.update_order_status(order_id, OrderStatus.RECEIVED.value)
        elif payment_status == 'Recusado':
            self.order_gateway.update_order_status(order_id, OrderStatus.FINALIZED.value)