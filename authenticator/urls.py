from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from . import views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('register/', views.RegisterView.as_view(), name='resiter-user')
]