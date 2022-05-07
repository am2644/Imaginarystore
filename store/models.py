from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


class Collection(models.Model):
    title = models.CharField(max_length=55)


class Product(models.Model):
    title = models.CharField(max_length=55)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name='products')


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_DIAMOND = 'D'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_DIAMOND, 'Diamond')
    ]
    name = models.CharField(max_length=55)
    email = models.EmailField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, validators=[
                             MinLengthValidator(11)])
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Address(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=501)

    class Meta:
        unique_together = ('customer', 'address')
