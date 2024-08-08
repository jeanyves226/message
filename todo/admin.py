from django.contrib import admin
from .models import Todo
from django.db import models
from django.contrib.auth import get_user_model
from image_uploader_widget.widgets import ImageUploaderWidget
from reversion.admin import VersionAdmin
from unfold.admin import ModelAdmin

User = get_user_model()

@admin.register(Todo)
class TodoAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'user')
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
