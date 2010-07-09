from django.db import models
from nomadblog.models import Post


class WebsitePost(Post):
    """
    Subclassing ``Post`` you can add more fields to your model, like this
    ``summary``. Pass this model to the nomadblog views using the ``model``
    parameter in ``kwargs`` (see ``website.blog_urls``).
    """
    summary = models.TextField()

    def __unicode__(self):
        return self.post_ptr.title

