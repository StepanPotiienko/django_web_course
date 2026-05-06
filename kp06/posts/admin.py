from django.contrib import admin
from .models import Post, Measurement

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("text", "date", "temperature", "wind_speed")
