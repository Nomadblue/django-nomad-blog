from django.db import models
from django.contrib.auth.models import User
import settings

NOMADBLOG_MULTIPLE_BLOGS = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False) 


try:
    from settings import POST_STATUS_CHOICES
except ImportError:
    PUBLIC_STATUS = 0
    DRAFT_STATUS = 1
    PRIVATE_STATUS = 2
    POST_STATUS_CHOICES = (
        (PUBLIC_STATUS, 'public'),
        (DRAFT_STATUS, 'draft'),
        (PRIVATE_STATUS, 'private'),
    )


class Blog(models.Model):
    users = models.ManyToManyField(User, through='BlogUser')
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.title

    @models.permalink
    def get_absolute_url(self):
        filters = {}
        if NOMADBLOG_MULTIPLE_BLOGS:
            filters['blog_slug'] = self.slug
        return ('list_posts', (), filters)


class BlogUser(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return u"%s - %s" % (self.user, self.blog)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    bloguser = models.ForeignKey(BlogUser)
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS_CHOICES, default=0)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category)
    content = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        filters = {'category': self.category.name, 'slug': self.slug}
        if NOMADBLOG_MULTIPLE_BLOGS:
            filters['blog_slug'] = self.bloguser.blog.slug
        return ('show_post', (), filters)

    def __unicode__(self):
        return "%s - %s" % (self.bloguser, self.title)

