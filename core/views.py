from django.shortcuts import render
from django.views import generic
from core.models import Blogger, BlogPost, Topic

# Create your views here.

def index(request):
    """View function for home page of Blog Site."""
    # Generate counts of blog posts and comments
    num_posts = BlogPost.objects.all().count()
    # num_comments = Comments.object.all().count() <--when it exists

    # Blogger count
    num_bloggers = Blogger.objects.count()

    context = {
        'num_posts': num_posts,
        'num_bloggers': num_bloggers,
    }
    #Render the HTML template index.html with data in the context variable
    return render(request, 'index.html', context=context)

def bloggerlist(request):
    """View function for list of all writers"""
    return render(request, 'blogger-list.html')

def blogpostdetail(request):
    """View function for detail view of individual post"""
    return render(request, 'blogpost-detail.html')

class BlogPostView(generic.ListView):
    model = BlogPost
    template_name = 'index.html'

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blogpost-detail.html'

class BloggerListView(generic.ListView):
    model = Blogger
    template_name = 'blogger-list.html'

class BloggerDetailView(generic.DetailView):
    model = Blogger
    template_name = 'blogger-detail.html'
