from django.contrib import admin
from .models import Product, Offer


class ProductAdmain(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmain(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmain)
admin.site.register(Offer, OfferAdmain)