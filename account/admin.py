from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_staff']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"),
         {"fields":(
             "first_name",
             "last_name",
             "middle_name",
             "email")
          }
         ),
        (_("Permissions"),
         {"fields":(
             "is_active",
             "is_staff",
             "is_superuser",
             "groups",
             "user_permissions",
             ),
          },
         ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Custom info"), {"fields": ("photo",)}),
    )