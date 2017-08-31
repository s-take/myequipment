# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Equipment, Rental
from .serializers import UserSerializer, EquipmentSerializer, RentalSerializer
from rest_framework import permissions

# Create your views here.
def rental_list(request):
    """貸出一覧"""
    rentals = Rental.objects.all().order_by('equipment', '-id').distinct('equipment_id') # only postgresql

    return render(request,
                  'rentals/rental_list.html',
                  {'rentals': rentals})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('nfc_id',)
    permission_classes = (permissions.IsAuthenticated,)


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_fields = ('barcode',)
    permission_classes = (permissions.IsAuthenticated,)


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all().order_by('-created_at')
    serializer_class = RentalSerializer
    filter_fields = ('equipment', 'user')
    permission_classes = (permissions.IsAuthenticated,)