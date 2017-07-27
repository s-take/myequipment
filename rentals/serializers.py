# coding: utf-8
from rest_framework import serializers
from .models import User, Equipment, Rental


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('employee_no', 'name')


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('barcode', 'name', 'manage_no', 'manage_user', 'comment')


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'equipment', 'user', 'processing', 'created_at')