from django.contrib import admin
from .models import Products, Stock, StockProduct

admin.site.register(Products)
admin.site.register(Stock)
admin.site.register(StockProduct)