from django.contrib import admin
from .models import Blog  # , Comment

class BlogAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "author")
	list_filter = ("is_published", "created_time", "author")
	search_fields = ("title", "body", "slug", "author")
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
# admin.site.register(Comment)