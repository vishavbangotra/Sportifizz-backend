from django.urls import path
from .views import ListProducts, DetailProduct, UpdateProductView, CreateProductView, DeleteProductView
urlpatterns = [
    path('products/', ListProducts, name='Product_list'),
    path('products/<str:pk>/', DetailProduct, name='Product_detail'),
    path('products/<str:pk>/edit/', UpdateProductView, name='Product_update'),
    path('products/<str:pk>/edit/', UpdateProductView, name='Product_update'),
    path('products/<str:pk>/remove/', DeleteProductView, name='Product_remove'),
    path('products/create/', CreateProductView, name='Product_create'),


]
