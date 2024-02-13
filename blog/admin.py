from django.contrib import admin
from django.contrib import admin

from blog.models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "username", "post_count", "password"]
    search_fields = ["first_name", "username", "last_name"]
    list_display_links = ["username", "password"]

    def get_post_count(self):
        return self.post_count


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "is_active", "published", "created_at", "updated_at"]
    search_fields = ["title", "content"]
    list_filter = ["author", "is_active"]
    date_hierarchy = "published"
