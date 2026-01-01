from django.contrib import admin
from .models import Post


@admin.register(Post)  # Equivalent to `admin.site.register(Post, PostAdmin)`
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "is_published",
        "created_at",
    )  # Controls columns shows in the admin list page
    prepopulated_fields = {
        "slug": ("title",)
    }  # Automatically generate the slug field from the title field
