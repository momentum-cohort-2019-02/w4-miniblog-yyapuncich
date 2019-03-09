from django.contrib import admin
from core.models import Blogger, BlogPost, Topic

# Register your models here.

admin.site.register(Topic)
admin.site.register(Blogger)
admin.site.register(BlogPost)
