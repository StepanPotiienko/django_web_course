from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "date",
        "temperature",
        "pressure",
        "wind_speed",
        "precipitation_probability",
    )
