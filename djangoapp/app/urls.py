from django.urls import path, include
from app.views import BlogPostList

urlpatterns = [
    path('', BlogPostList.as_view(), name='post-list')
]