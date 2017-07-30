from django.contrib import admin
from rentals.models import User, Equipment, Rental

# Register your models here.

#admin.site.register(User)
#admin.site.register(Equipment)

class UserAdmin(admin.ModelAdmin):
    list_display = ('nfc_id', 'employee_no', 'name',)
    list_display_links = ('nfc_id', 'employee_no', 'name',)
admin.site.register(User, UserAdmin)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'name', 'manage_no', 'manage_user', 'comment',)
    list_display_links = ('barcode', 'name',)
admin.site.register(Equipment, EquipmentAdmin)


class RentalAdmin(admin.ModelAdmin):
    readonly_fields = ('user_name', 'equipment_name',)

    def user_name(self, obj):
        return obj.user.name

    def equipment_name(self, obj):
        return obj.equipment.name

    list_display = ('equipment_name', 'user_name', 'processing', 'created_at',)
admin.site.register(Rental, RentalAdmin)