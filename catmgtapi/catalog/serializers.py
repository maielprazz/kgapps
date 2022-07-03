from rest_framework import serializers
from .models import Product, Banner, Category
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('title', 'image','parent')

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Banner
    fields = '__all__'






# class ProductSerializer(serializers.ModelSerializer):
#   email = serializers.EmailField(max_length = 255, min_length = 3)
#   password = serializers.CharField(max_length = 68, min_length = 6, write_only = True)
#   username = serializers.CharField(max_length = 255, min_length = 3, read_only  = True)
#   tokens = serializers.CharField(read_only  = True)

#   class Meta:
#     model = User
#     fields = ['email','password', 'username', 'tokens']

#   def validate(self, attrs):
#     email = attrs.get('email','')
#     password = attrs.get('password','')
 
#     user = auth.authenticate(email= email, password=password)
#     if not user :
#       raise AuthenticationFailed('Invalid credentials, try again')

#     return {
#       'email': user.email,
#       'username': user.username,
#       'tokens': user.tokens(),
    
#     }