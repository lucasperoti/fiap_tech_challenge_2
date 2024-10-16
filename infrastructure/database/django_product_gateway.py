from interface_adapters.gateways.product_gateway import ProductGateway
from infrastructure.django_app.products.models import Product as ORMProduct, Category as ORMCategory
from core.entities.models import Product, Category

class DjangoProductGateway(ProductGateway):
    def list_all_products(self) -> list:
        orm_products = ORMProduct.objects.all()
        return [self._map_orm_to_entity(orm_product) for orm_product in orm_products]

    def list_products_by_category(self, category_name: str) -> list:
        orm_products = ORMProduct.objects.filter(category__name=category_name)
        return [self._map_orm_to_entity(orm_product) for orm_product in orm_products]

    def get_product_by_id(self, product_id: int) -> Product:
        orm_product = ORMProduct.objects.get(id=product_id)
        return self._map_orm_to_entity(orm_product)

    def create_product(self, product_data: dict) -> Product:
        category_data = product_data.pop('category')
        category, _ = ORMCategory.objects.get_or_create(name=category_data['name'])
        orm_product = ORMProduct.objects.create(category=category, **product_data)
        return self._map_orm_to_entity(orm_product)

    def _map_orm_to_entity(self, orm_product: ORMProduct) -> Product:
        category = Category(
            id=orm_product.category.id,
            name=orm_product.category.name
        )
        return Product(
            id=orm_product.id,
            name=orm_product.name,
            description=orm_product.description,
            price=orm_product.price,
            category=category,
            image_url=orm_product.image.url if orm_product.image else None
        )