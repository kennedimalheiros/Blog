from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'is_staff', 'is_active', 'phone',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        ('Informações do Usuário', {'fields': ('first_name', 'last_name', 'email', 'password', 'phone', 'avatar',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('Informações do Usuário', {
            'classes': ('wide',),
            'fields': ('first_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
