from django.contrib import admin
from django.utils.html import format_html
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('email',)
    list_per_page = 8

admin.site.register(CustomUser, UserAdmin)