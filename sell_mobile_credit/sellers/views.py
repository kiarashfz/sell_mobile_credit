from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView

from sellers.models import Seller
from sellers.serializers import SellerSerializer, SellerAccountingSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerAccountingAPIView(RetrieveAPIView):
    serializer_class = SellerAccountingSerializer

    def get_object(self):
        return Seller.objects.get(id=self.kwargs['pk'])
