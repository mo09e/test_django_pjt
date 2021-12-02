from django.contrib import admin

from core_dir.blog.models import Author, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ()

