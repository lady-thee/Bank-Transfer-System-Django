from django.contrib import admin
from customers.models import Customers



class CustomersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'current_balance')



admin.site.register(Customers, CustomersAdmin)

