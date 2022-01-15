from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'location')
    list_filter = ('email', 'is_staff', 'is_active', 'location')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'location')}),
        ('Permissions', {'fields':('is_staff','is_active')})
    )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
            ),
        )
    search_fields = ('email',)
    ordering = ('email',)



admin.site.register(User, CustomUserAdmin)
