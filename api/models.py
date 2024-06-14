from django.db import models
from datetime import datetime

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.email} - {self.telephone}"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.OneToOneField(ContactInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    date = models.DateTimeField(default=datetime.now)
    suppliers = models.ManyToManyField(Supplier, related_name='items')

    def __str__(self):
        return self.name
