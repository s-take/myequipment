# coding: utf-8
from django.conf.urls import url
from . import views
from rest_framework import routers
from .views import UserViewSet, EquipmentViewSet, RentalViewSet

urlpatterns = [
    url(r'^rental/$', views.rental_list, name='rental_list'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'equipments', EquipmentViewSet)
router.register(r'rentals', RentalViewSet)