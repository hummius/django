from django.contrib import admin

from app_market.models import Market, Order, Product, ItemPosition, Offer, Promotion


class MarketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


class ItemPositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'product', 'market']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_price', 'created_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'created_at']


class PromotionAdmin(admin.ModelAdmin):
    list_display = ['id', 'promotion', 'product']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'offer']


admin.site.register(Market, MarketAdmin)
admin.site.register(ItemPosition, ItemPositionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Promotion, PromotionAdmin)

