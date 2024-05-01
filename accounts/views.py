from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class profileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        articles = User.objects.all()
        serializer = UserSerializer(articles, many=True)
        return Response(serializer.data)

from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer