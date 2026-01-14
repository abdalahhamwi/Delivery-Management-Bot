from django.db import models

# Create your models here.


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "PD", "Pending"
        DELIVERED = "DF", "Delivered"

    adderss = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=OrderStatus,default=OrderStatus.PENDING)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id