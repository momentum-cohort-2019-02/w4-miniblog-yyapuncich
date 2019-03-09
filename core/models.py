from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, time
from PIL import Image

# Create your models here.

class Blogger(models.Model):
    """Defines a Blogpost author"""
    name = models.CharField(max_length=50, help_text='Enter your name as you would like it displayed.')
    profile_pic = models.ImageField('Photo')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns url to access particular blogger instance"""
        return reverse("blogger-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Blogger model object"""
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the topic for your blog post')

    def __str__(self):
        """String representing Topic model object."""
        return self.name   

class BlogPost(models.Model):
    title = models.CharField(max_length=50, help_text='Enter the title for your post.')
    blog_entry = models.TextField('Thoughts!', )
    blogger = models.ForeignKey(Blogger,  on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField(Topic, help_text='Select a topic.')

    def get_absolute_url(self):
        """Returns url for accessing specific blog post"""
        return reverse("blog-post-detail", args=[str(self.id)])
    

    def __str__(self):
        return self.blog_entry

# class Comment(models.Model):
