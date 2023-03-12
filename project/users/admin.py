from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ("email",)
    list_display = (
        "id",
        "email",
        "date_of_birth",
        "is_active",
        "is_staff",
        "date_joined",
    )
