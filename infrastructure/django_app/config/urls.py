from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API de Autoatendimento da Lanchonete",
      default_version='v1',
      description="Documentação da API para o sistema de autoatendimento",
      contact=openapi.Contact(email="suporte@lanchonete.com"),
   ),
   public=True,
   permission_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', include('infrastructure.django_app.orders.urls')),
    path('api/customers/', include('infrastructure.django_app.customers.urls')),
    path('api/products/', include('infrastructure.django_app.products.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]