from dataclasses import field
from venv import create
from rest_framework.serializers import ModelSerializer

from .models import Product

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'catagory', 'image', 'price', 'discount', 'quantity', 'created_by', 'delivary_option']