from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactList(admin.ModelAdmin):
    list_display = (
        'Name',
        'Email',
        'Subject',
        'Message',
    )


admin.site.register(Contact,ContactList)
