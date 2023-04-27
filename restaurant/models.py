from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()


class Booking(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
