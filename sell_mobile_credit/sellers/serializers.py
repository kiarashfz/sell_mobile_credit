from rest_framework import serializers

from sellers.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name', 'credit')
        read_only_fields = ('created_at', 'updated_at', 'credit')


class SellerAccountingSerializer(serializers.ModelSerializer):
    is_calculations_correct = serializers.BooleanField()
    total_charged_credit = serializers.IntegerField()
    total_buy_amount = serializers.IntegerField()
    calculation_error_amount = serializers.IntegerField(source='get_calculation_error_amount')

    class Meta:
        model = Seller
        fields = ('id', 'name', 'credit', 'is_calculations_correct', 'total_charged_credit', 'total_buy_amount',
                  'calculation_error_amount')
        read_only_fields = ('created_at', 'updated_at', 'credit')
