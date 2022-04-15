from django.contrib import admin
from .models import Company, Product, ProductSite, ProductSize, Category, Comment

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.register(Category)
admin.site.register(Comment)

