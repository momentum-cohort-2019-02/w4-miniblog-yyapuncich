from django.contrib import admin
from core.models import Blogger, BlogPost, Topic

# Register your models here.
class BlogPostInline(admin.TabularInline):
    model = BlogPost

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_pic')
    inlines = [BlogPostInline]

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_blog_entry', 'display_topic', 'blogger', 'date_created')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
