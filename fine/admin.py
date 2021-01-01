from django.contrib import admin

# Register your models here.
from .models import Product , Inquiry

admin.site.register(Product)
admin.site.register(Inquiry)