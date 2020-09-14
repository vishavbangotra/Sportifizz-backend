from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def ListProducts(request):
    if request.method == 'GET':
        Products = Product.objects.all()
        ProductsResponse = ProductSerializer(Products, many=True)
        return Response(ProductsResponse.data)

@api_view(['GET'])
def DetailProduct(request,pk):
    product = get_object_or_404(Product,pk=pk)
    ProductsResponse = ProductSerializer(product, many=False)
    return Response(ProductsResponse.data)


@api_view(['POST'])
def CreateProductView(request,pk):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteProductView(request,pk):
    product = get_object_or_404(Product,pk=pk)
    product.delete()
    return redirect('/')

@api_view(['PUT', 'GET'])
def UpdateProductView(request, pk):
    product = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(data=request.data, instance=product)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
