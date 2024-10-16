from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]