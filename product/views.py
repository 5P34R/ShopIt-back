from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer

class Products(APIView):

    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductListSerializer(obj, many=True)
        return Response(serializer.data)