from django.contrib import admin
from core.models import Blogger, BlogPost, Topic

# Register your models here.

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_blog_entry', 'display_topic', 'blogger', 'date_created')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ()
