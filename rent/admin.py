from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ("id", "login", "gmail", "phone", "first_name", "last_name", "is_staff", "is_superuser", "is_blocked", "created_at")
    list_filter = ("is_staff", "is_superuser", "is_blocked")
    search_fields = ("login", "gmail", "phone", "first_name", "last_name")

    # Use 'login' instead of 'username'
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("login", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "gmail", "phone")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "is_blocked", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("login", "gmail", "phone", "first_name", "last_name", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )
