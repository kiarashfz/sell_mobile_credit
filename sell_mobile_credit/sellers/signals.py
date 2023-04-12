from django.db.models.signals import post_save
from django.dispatch import receiver

from sellers.models import SellerCreditOrder


@receiver(post_save, sender=SellerCreditOrder)
def increase_seller_credit(sender, instance, created, **kwargs):
    if created:
        instance.seller.credit += instance.amount
        instance.seller.save()
