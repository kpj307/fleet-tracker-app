from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Vehicle(models.Model):
    plate = models.CharField(max_length=100)
    make = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehicles")

    def __str__(self):
        return self.plate_number
        

class Income(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField(default=now)


class Expense(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField(default=now)