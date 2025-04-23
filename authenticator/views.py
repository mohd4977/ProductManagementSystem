from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import MyTOPS, RegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTOPS

class RegisterView(generics.CreateAPIView):
    queryset  = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

# Create your views here.
