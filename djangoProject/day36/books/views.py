from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from .serializers import BookInfoSerializer


class BookInfoAPIView(ModelViewSet):
    # 告诉当前视图，要从哪个模型类中查数据 AOP：面向切面编程
    queryset = BookInfo.objects.all()
    # 告诉视图，谁是你的序列化类 AOP：面向切面编程
    serializer_class = BookInfoSerializer
