from django.db import models

from core.models import BaseModel


class Seller(BaseModel):
    name = models.CharField(max_length=63)
    credit = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.name
