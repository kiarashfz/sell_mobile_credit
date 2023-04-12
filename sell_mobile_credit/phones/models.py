from django.core.exceptions import ValidationError
from django.db import models

from core.models import BaseModel


class SimCard(BaseModel):
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Sim Card'
        verbose_name_plural = 'Sim Cards'

    number = models.CharField(max_length=15)
    credit = models.PositiveIntegerField(default=0, editable=False)

    def increase_sim_card_credit(self, amount: int):
        self.credit += amount
        self.save()

    def __str__(self):
        return self.number


class SimCreditOrder(BaseModel):
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Sim Card Credit Order'
        verbose_name_plural = 'Sim Card Credit Orders'

    sim_card = models.ForeignKey(SimCard, on_delete=models.CASCADE)
    seller = models.ForeignKey("sellers.Seller", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.sim_card} - {self.amount} - {self.seller}'

    def clean(self):
        # check if amount updated
        if self.id:
            old_amount = SimCreditOrder.objects.get(id=self.id).amount
            if old_amount != self.amount:
                raise ValidationError({'amount': "You can't change the amount."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
