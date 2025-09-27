from django.contrib import admin

# Register your models here.
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # optional: show these columns in admin list
