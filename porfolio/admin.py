from django.contrib import admin
from .models import UserContact, MessageContact
# Register your models here.
admin.site.register(UserContact)
admin.site.register(MessageContact)