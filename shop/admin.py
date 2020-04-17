from django.contrib import admin


from .models import ProductCategory, Products, Contact, Orders, OrderUpdate

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)