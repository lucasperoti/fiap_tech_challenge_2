from interface_adapters.gateways.order_gateway import OrderGateway
from infrastructure.django_app.orders.models import Order as ORMOrder, OrderItem as ORMOrderItem
from core.entities.models import Order, OrderItem, OrderStatus
from infrastructure.django_app.customers.models import Customer as ORMCustomer
from infrastructure.django_app.products.models import Product as ORMProduct
from core.entities.models import Customer, Product, Category

class DjangoOrderGateway(OrderGateway):
    def save_order(self, order: Order) -> Order:
        orm_order = ORMOrder.objects.create(
            customer=ORMCustomer.objects.get(id=order.customer.id) if order.customer else None,
            status=order.status.value,
            payment_status=order.payment_status
        )
        for item in order.items:
            ORMOrderItem.objects.create(
                order=orm_order,
                product=ORMProduct.objects.get(id=item.product.id),
                quantity=item.quantity
            )
        order.id = orm_order.id
        return order

    def update_order_status(self, order_id: int, new_status: str):
        orm_order = ORMOrder.objects.get(id=order_id)
        orm_order.status = new_status
        orm_order.save()

    def update_payment_status(self, order_id: int, payment_status: str):
        orm_order = ORMOrder.objects.get(id=order_id)
        orm_order.payment_status = payment_status
        orm_order.save()

    def list_orders(self) -> list:
        orm_orders = ORMOrder.objects.exclude(status=OrderStatus.FINALIZED.value)
        # Ordenar conforme regras
        status_priority = {
            OrderStatus.READY.value: 0,
            OrderStatus.PREPARING.value: 1,
            OrderStatus.RECEIVED.value: 2,
        }
        orm_orders = sorted(orm_orders, key=lambda x: (status_priority.get(x.status, 3), x.created_at))
        orders = [self._map_orm_to_entity(orm_order) for orm_order in orm_orders]
        return orders

    def get_order_by_id(self, order_id: int) -> Order:
        orm_order = ORMOrder.objects.get(id=order_id)
        return self._map_orm_to_entity(orm_order)

    def _map_orm_to_entity(self, orm_order: ORMOrder) -> Order:
        customer = None
        if orm_order.customer:
            customer = Customer(
                id=orm_order.customer.id,
                cpf=orm_order.customer.cpf,
                name=orm_order.customer.name,
                email=orm_order.customer.email
            )
        items = []
        for orm_item in orm_order.items.all():
            product = Product(
                id=orm_item.product.id,
                name=orm_item.product.name,
                description=orm_item.product.description,
                price=orm_item.product.price,
                category=Category(
                    id=orm_item.product.category.id,
                    name=orm_item.product.category.name
                ),
                image_url=orm_item.product.image.url if orm_item.product.image else None
            )
            item = OrderItem(
                product=product,
                quantity=orm_item.quantity
            )
            items.append(item)
        order = Order(
            id=orm_order.id,
            customer=customer,
            items=items,
            status=OrderStatus(orm_order.status),
            payment_status=orm_order.payment_status,
            created_at=orm_order.created_at
        )
        return order