from rest_framework import serializers

from phones.models import SimCreditOrder, SimCard


class ChargeSimCreditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimCreditOrder
        fields = ('id', 'sim_card', 'seller', 'amount')
        read_only_fields = ('created_at', 'updated_at')


class SimCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimCard
        fields = ('id', 'number', 'credit')
        read_only_fields = ('created_at', 'updated_at', 'credit')
