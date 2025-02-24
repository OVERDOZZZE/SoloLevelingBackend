from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    # Extend UserAdmin fieldsets to include custom fields
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": (
            "bio", "date_of_birth", "overall_exp", "level", "achievements", "skills", "user_image"
        )}),
    )
    # Fields for user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": (
            "bio", "date_of_birth", "overall_exp", "level", "achievements", "skills", "user_image"
        )}),
    )
