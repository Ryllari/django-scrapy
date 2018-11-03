from django.db import models

class BlogPost(models.Model):
    """
    This class represents a BlogPost
    A BlogPost contains information about a Post on Blog

    :cvar str title: post's title
    :cvar str short_text: post's short_text
    :cvar datetime posted_at: post's timestamp posted
    """
    title = models.TextField()
    short_text = models.TextField()
    posted_at = models.DateTimeField()