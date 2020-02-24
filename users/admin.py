from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("superhost", "currency", "superhost")
