from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, time
from PIL import Image
import uuid

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

# Photos used for profiles: 
# Photo by hannah grace on Unsplash(lady with sunglasses and pink jacket)
# Photo by Mohammad Faruque on Unsplash(lady with tattoos on back)
# Photo by Sai De Silva on Unsplash(lady with daughter)
# Photo by Seth Doyle on Unsplash(guy with glasses)
    
class Topic(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the topic for your blog post')

    def __str__(self):
        """String representing Topic model object."""
        return self.name   

class BlogPost(models.Model):
    title = models.CharField(max_length=50, help_text='Enter the title for your post.')
    blog_entry = models.TextField('Thoughts!')
    blogger = models.ForeignKey(Blogger,  on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField(Topic, help_text='Select a topic.')
    date_created = models.DateTimeField('post date')

    def get_absolute_url(self):
        """Returns url for accessing specific blog post"""
        return reverse("blogpost-detail", args=[str(self.id)])

    def display_blog_entry(self):
        """Create a string for the Blog entry. This is required to display blog snippet in Admin."""
        return self.blog_entry[:75] + "..."

    def display_topic(self):
        """Returns topic for display on list of blog entries in admin"""
        return ', '.join(topic.name for topic in self.topic.all()[:3])

    class Meta:
        ordering = ['date_created']

    display_blog_entry.short_description = 'Blog Post'
    display_topic.short_description = "Topics"

    def __str__(self):
        return self.blog_entry

class Comment(models.Model):
    """Model representing individual comments by users who are authenticated with logins"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular comment across site.')
    blog_entry = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, help_text='Title for your comments')
    date_posted = models.DateTimeField('commented on', auto_now=True)
    comment = models.TextField(max_length=200, help_text='Enter your lovely things to say!')

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        """String for representing the Comment Model object."""
        return f'{ self.title }{{ self.comment|truncatewords:15 }}'
