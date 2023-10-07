from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)