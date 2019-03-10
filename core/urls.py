from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostView.as_view(), name='index'),
    path('writers/', views.bloggerlist, name='blogger-list'),
    path('posts/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
]
