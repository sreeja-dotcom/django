from django.contrib import admin
from.models import Products
#admin.site.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
admin.site.register(Products,ProductsAdmin)
# Register your models here.
