from django.urls import path, include
from rest_framework.routers import DefaultRouter

from phones.views import ChargeSimCreditAPIView, SimCardViewSet

sim_card_router = DefaultRouter()
sim_card_router.register(r'sim-cards', SimCardViewSet, basename='simcard')

urlpatterns = [
    path('charge-sim-credit/', ChargeSimCreditAPIView.as_view(), name='charge-sim-credit'),
    path('', include(sim_card_router.urls)),
]
