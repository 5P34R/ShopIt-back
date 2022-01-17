from django.db import models

from django.contrib.auth.models import User

DELIVARY_OPTIONS = (
    ('COD', 'COD'),
    ('Online Payment', 'Online Payment'),
    ('EMI', 'EMI')
)

class Catagory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    delivary_option = models.CharField(max_length=30, choices=DELIVARY_OPTIONS)


    def __str__(self):
        return self.title   