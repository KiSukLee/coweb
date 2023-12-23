from django.contrib import admin
from .models import User, Product, Inventory, Cart
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Cart)