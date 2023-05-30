from django.contrib import admin
from app_blogs.models import Blog, Post, Author, Moderator


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Moderator, ModeratorAdmin)

