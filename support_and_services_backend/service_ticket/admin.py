from django.contrib import admin
# from connection.models import Customer, Technician
from .models import Ticket

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('customer_id', 'name', 'email_address', 'phone_number', 'address_line1', 'address_line2')
#     search_fields = ('name', 'email_address', 'phone_number', 'address_line1', 'address_line2')

# @admin.register(Technician)
# class TechnicianAdmin(admin.ModelAdmin):
#     list_display = ('technician_id', 'first_name', 'last_name')
#     search_fields = ('first_name', 'last_name')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'customer', 'status', 'priority', 'created_at', 'subject')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('customer__name', 'subject', 'status')
