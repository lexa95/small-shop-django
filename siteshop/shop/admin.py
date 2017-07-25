from django.contrib import admin
from .models import Product, Delivery, Order


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('date_created', )
    list_display = ("product", "status", "count_product", "date_created", )


admin.site.register(Product, ProductAdmin)
admin.site.register(Delivery)
admin.site.register(Order, OrderAdmin)
