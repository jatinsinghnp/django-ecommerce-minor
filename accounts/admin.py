from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import (UserChangeForm,UserCreationForm)
from .models import ShopUser
# Register your models here.


@admin.register(ShopUser)
class ShopAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',  'is_active','is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
       # ('Full name', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin',  'is_active','is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
