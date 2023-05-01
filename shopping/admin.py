from django.contrib import admin
from .models import shopping_index,Shopping_detail,cart

# Register your models here.
admin.site.register(shopping_index)
admin.site.register(Shopping_detail)
admin.site.register(cart)