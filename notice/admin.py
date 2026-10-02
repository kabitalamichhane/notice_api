from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "priority", "is_active", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["category", "priority", "is_active"]
