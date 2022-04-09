from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    Address = models.CharField(max_length=400)
    date_ordered = models.DateTimeField(auto_now_add=True)
    customer_order = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_order
