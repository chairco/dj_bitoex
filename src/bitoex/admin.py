from django.contrib import admin

from .models import Bitoex


@admin.register(Bitoex)
class BitoexAdmin(admin.ModelAdmin):
    list_display = ['buy', 'sell', 'timestamp', 'created_at']