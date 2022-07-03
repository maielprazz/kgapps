from django.shortcuts import render
from rest_framework import generics, status
from .serializers import LoginSerializer, RegisterSerializer 
from rest_framework.response import Response


class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
    # print (request.data)
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request):
    user = request.data
    serializer = self.serializer_class(data = user)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    user_data = serializer.data

    return Response(user_data, status=status.HTTP_201_CREATED)