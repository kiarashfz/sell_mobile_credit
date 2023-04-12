from django.db import transaction, IntegrityError
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView

from phones.models import SimCard
from phones.serializers import ChargeSimCreditSerializer, SimCardSerializer


class ChargeSimCreditAPIView(CreateAPIView):
    serializer_class = ChargeSimCreditSerializer

    # increase sim card credit and decrease seller credit and create charge order in one transaction
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                data = serializer.validated_data
                sim_card, seller, amount = data['sim_card'], data['seller'], data['amount']
                seller.buy_sim_card_credit(sim_card, amount)
                super().perform_create(serializer)
        except IntegrityError:
            raise APIException('Seller does not have enough credit.', code=status.HTTP_400_BAD_REQUEST)


class SimCardViewSet(viewsets.ModelViewSet):
    queryset = SimCard.objects.all()
    serializer_class = SimCardSerializer
