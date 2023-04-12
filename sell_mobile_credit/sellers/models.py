from django.core.exceptions import ValidationError
from django.db import models

from core.models import BaseModel
from phones.models import SimCreditOrder


class Seller(BaseModel):
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    name = models.CharField(max_length=63)
    credit = models.PositiveIntegerField(default=0, editable=False)

    def buy_sim_card_credit(self, sim_card, amount: int):
        sim_card.increase_sim_card_credit(amount)
        self.decrease_seller_credit(amount)

    def decrease_seller_credit(self, amount: int):
        self.credit -= amount
        self.save()

    def is_calculations_correct(self):
        # check if seller credit is correct
        if self.get_calculation_error_amount() != 0:
            return False
        return True

    def get_calculation_error_amount(self):
        # check if seller credit is correct
        total_amount = self.total_charged_credit - self.total_buy_amount
        if total_amount != self.credit:
            return self.credit - total_amount
        return 0

    @property
    def total_charged_credit(self):
        return self.sellercreditorder_set.aggregate(models.Sum('amount'))['amount__sum']

    @property
    def total_buy_amount(self):
        return self.simcreditorder_set.aggregate(models.Sum('amount'))['amount__sum']

    def __str__(self):
        return self.name


class SellerCreditOrder(BaseModel):
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Seller Credit Order'
        verbose_name_plural = 'Seller Credit Orders'

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.seller} - {self.amount}'

    def clean(self):
        # check if amount updated
        if self.id:
            old_amount = SellerCreditOrder.objects.get(id=self.id).amount
            if old_amount != self.amount:
                raise ValidationError({'amount': "You can't change the amount."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
