from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display=['productname','price','stock']
	list_filter = ['price']
	prepulated_fields={'slug':('name',)}
admin.site.register(Product,ProductAdmin)
