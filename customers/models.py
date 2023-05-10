from django.db import models
import uuid 
from django.contrib.auth.models import User 


class Customers(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    birthday = models.DateTimeField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return  str(self.current_balance)
    