from django.contrib import admin
from rentals.models import User, Equipment

# Register your models here.

#admin.site.register(User)
#admin.site.register(Equipment)

class UserAdmin(admin.ModelAdmin):
    list_display = ('employee_no', 'name',)
    list_display_links = ('employee_no', 'name',)
admin.site.register(User, UserAdmin)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'name', 'manage_no', 'manage_user', 'comment',)
    list_display_links = ('barcode', 'name',)
admin.site.register(Equipment, EquipmentAdmin)