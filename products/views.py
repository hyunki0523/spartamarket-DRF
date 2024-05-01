from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductListAPIView(APIView):
    def get(self, request):
        articles = Product.objects.all()
        serializer = ProductSerializer(articles, many=True)
        return Response(serializer.data)

class ProducCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        if Product.author != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        if Product.author == request.pk:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

