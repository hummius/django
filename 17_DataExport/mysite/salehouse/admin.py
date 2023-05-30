from django.contrib import admin

from salehouse.models import SaleHouse, RoomType, NumberOfRooms, SaleHouseNews


class SaleHouseNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class SaleHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']


class NumbersOfRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']


admin.site.register(SaleHouseNews, SaleHouseNewsAdmin)
admin.site.register(SaleHouse, SaleHouseAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(NumberOfRooms, NumbersOfRoomAdmin)

