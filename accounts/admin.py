from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', ]

admin.site.register(Customer, CustomerAdmin)