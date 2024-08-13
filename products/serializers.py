from rest_framework import serializers
from .models import Product


class ProductSerialazers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']
