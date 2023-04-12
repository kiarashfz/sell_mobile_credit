from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sellers.views import SellerViewSet, SellerAccountingAPIView

sellers_router = DefaultRouter()
sellers_router.register(r'sellers', SellerViewSet, basename='seller')

urlpatterns = [
    path('', include(sellers_router.urls)),
    path('accounting/<int:pk>/', SellerAccountingAPIView.as_view(), name='seller-accounting'),
]
