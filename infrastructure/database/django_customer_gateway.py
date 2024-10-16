from interface_adapters.gateways.customer_gateway import CustomerGateway
from infrastructure.django_app.customers.models import Customer as ORMCustomer
from core.entities.models import Customer

class DjangoCustomerGateway(CustomerGateway):
    def list_customers(self) -> list:
        orm_customers = ORMCustomer.objects.all()
        return [self._map_orm_to_entity(orm_customer) for orm_customer in orm_customers]

    def get_customer_by_id(self, customer_id: int) -> Customer:
        orm_customer = ORMCustomer.objects.get(id=customer_id)
        return self._map_orm_to_entity(orm_customer)

    def create_customer(self, customer_data: dict) -> Customer:
        orm_customer = ORMCustomer.objects.create(**customer_data)
        return self._map_orm_to_entity(orm_customer)

    def get_or_create_customer(self, customer_data: dict) -> Customer:
        orm_customer, _ = ORMCustomer.objects.get_or_create(
            cpf=customer_data.get('cpf'),
            defaults={
                'name': customer_data.get('name'),
                'email': customer_data.get('email')
            }
        )
        return self._map_orm_to_entity(orm_customer)

    def _map_orm_to_entity(self, orm_customer: ORMCustomer) -> Customer:
        return Customer(
            id=orm_customer.id,
            cpf=orm_customer.cpf,
            name=orm_customer.name,
            email=orm_customer.email
        )