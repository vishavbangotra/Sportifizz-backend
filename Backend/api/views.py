from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def ListProducts(request):
    Products = Product.objects.all()
    ProductsResponse = ProductSerializer(Products)
