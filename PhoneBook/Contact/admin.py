

# Register your models here.
from django.contrib import admin
from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email_addr', 'street_addr')

admin.site.register(Contacts, ContactAdmin)