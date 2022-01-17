from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics

from .models import Product
from .serializers import ProductListSerializer

class Products(APIView):

    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductListSerializer(obj, many=True,  context={'request': request})
        return Response(serializer.data)


class ProductSearch(generics.ListCreateAPIView):
    search_fields = ['id', 'title']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer 