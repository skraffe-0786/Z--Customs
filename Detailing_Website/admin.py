from django.contrib import admin
from .models import Contact
from .models import Booking
# Register your models here.
admin.site.register(Contact)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = [
        'full_name',
        'phone',
        'vehicle',
        'service',
        'date',
        'time',
        'created_at'
    ]

    list_filter = ['vehicle','service','date']

    search_fields = ['full_name','email','phone']

    ordering = ['-created_at']