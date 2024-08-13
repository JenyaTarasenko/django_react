from django.shortcuts import render

from rest_framework import generics
from .models import Product
from .serializers import ProductSerialazers


class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialazers



class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialazers
    lookup_field = 'id'

