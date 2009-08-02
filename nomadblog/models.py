from django.db import models
from django.contrib.auth.models import User

try:
    from settings import NOMADBLOG_SINGLE_USER
except ImportError:
    NOMADBLOG_SINGLE_USER = False


class Blog(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s' % (self.user, self.title)

    @models.permalink
    def get_absolute_url(self):
        filters = {}
        if not NOMADBLOG_SINGLE_USER:
            filters['username'] = self.user.username
        return ('list_posts', (), filters)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    PUBLIC_STATUS = 0
    DRAFT_STATUS = 1
    PRIVATE_STATUS = 2
    STATUS_CHOICES = (
        (PUBLIC_STATUS, 'public'),
        (DRAFT_STATUS, 'draft'),
        (PRIVATE_STATUS, 'private'),
    )
    blog = models.ForeignKey(Blog)
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category)
    content = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        filters = {'category': self.category.name, 'slug': self.slug}
        if not NOMADBLOG_SINGLE_USER:
            filters['username'] = self.blog.user.username
        return ('show_post', (), filters)

    def __unicode__(self):
        return "%s - %s" % (self.blog.user, self.title)

