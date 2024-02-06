from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty forms to display for adding new comments inline

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'upvotes', 'time_added')
    search_fields = ['title', 'author']
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'upvotes', 'time_added')
    search_fields = ['text', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

