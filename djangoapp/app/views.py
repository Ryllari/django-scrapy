from django.views.generic import ListView

from app.models import BlogPost


class BlogPostList(ListView):
    model = BlogPost
    template_name = 'app/blogpost_list.html'
