from rest_framework import serializers

from restaurant.models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'