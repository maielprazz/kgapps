from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from .serializers import BannerSerializer, ProductSerializer, CategorySerializer
from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Product, Category, Banner
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated

# CATEGORY API

class CategoryListView(APIView):
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)

  def get(self,request):
    query = Category.objects.all()
    serializer_class = CategorySerializer(query, many = True)
    return Response(serializer_class.data)
  def post(self, request):
    print(request.data)
    serializer_obj = CategorySerializer(data=request.data)
    if serializer_obj.is_valid(raise_exception=True):
      category_saved = serializer_obj.save()
      return Response(request.data, status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryView(APIView):
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)

  def get(self,request, pid):
    query = Category.objects.filter(id = pid)
    serializer_class = CategorySerializer(query, many = True)
    return Response(serializer_class.data)

  def put(self, request, pid):
    category_obj = Category.objects.get(id = pid)
    serializer_obj = CategorySerializer(category_obj, data=request.data)
    if serializer_obj.is_valid(raise_exception=True):
      category_saved = serializer_obj.save()
      return Response(serializer_obj, status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pid):
    category_obj = Category.objects.get(id = pid).delete()
    return Response(status=status.HTTP_200_OK)


# PRODUCT API

class ProductListView(APIView):
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)

  def get(self,request):
    query = Product.objects.all()
    serializer_class = ProductSerializer(query, many = True)
    return Response(serializer_class.data)
  def post(self, request):
    print(request.data)
    serializer_obj = ProductSerializer(data=request.data)
    if serializer_obj.is_valid(raise_exception=True):
      product_saved = serializer_obj.save()
      return Response(request.data, status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)

  def get(self,request, pid):
    query = Product.objects.filter(id = pid)
    serializer_class = ProductSerializer(query, many = True)
    return Response(serializer_class.data)

  def put(self, request, pid):
    product_obj = Product.objects.get(id = pid)
    serializer_obj = ProductSerializer(product_obj, data=request.data)
    if serializer_obj.is_valid(raise_exception=True):
      product_saved = serializer_obj.save()
      return Response(serializer_obj, status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pid):
    product_obj = Product.objects.get(id = pid).delete()
    return Response(status=status.HTTP_200_OK)

# BANNER API

class BannerListView(APIView):
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)

  def get(self,request):
    query = Banner.objects.all()
    serializer_class = BannerSerializer(query, many = True)
    return Response(serializer_class.data)
  def post(self, request):
    print(request.data)
    serializer_obj = BannerSerializer(data=request.data)
    if serializer_obj.is_valid(raise_exception=True):
      banner_saved = serializer_obj.save()
      return Response(request.data, status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class BannerView(APIView):
  parser_classes = (MultiPartParser, FormParser, JSONParser)
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)

  def get(self,request, pid):
    query = Banner.objects.filter(id = pid)
    serializer_class = BannerSerializer(query, many = True)
    return Response(serializer_class.data)

  def put(self, request, pid):
    banner_obj = Banner.objects.get(id = pid)
    serializer_obj = BannerSerializer(banner_obj, data=request.data)
    if serializer_obj.is_valid(raise_exception=True):
      banner_saved = serializer_obj.save()
      return Response(serializer_obj, status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pid):
    banner_obj = Banner.objects.get(id = pid).delete()
    return Response(status=status.HTTP_200_OK)

