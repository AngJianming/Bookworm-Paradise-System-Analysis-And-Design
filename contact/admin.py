""" File specyfying settings for the admin panel. """
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    ''' Class defying how info from the Contact model displays in Admin '''
    list_display = (
        'full_name',
        'email',
        'message',
        'sent_on',
    )


admin.site.register(Contact, ContactAdmin)
