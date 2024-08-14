from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, TrailerRentalRequest
from .forms import DriverCreationForm

class UserAdmin(BaseUserAdmin):
    add_form = DriverCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'role', 'is_active')
    list_filter = ('role', 'is_staff')
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        if not change:  # When creating a new user
            obj.role = 'driver'
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
admin.site.register(TrailerRentalRequest)
