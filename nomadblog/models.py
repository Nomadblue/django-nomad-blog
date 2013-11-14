from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

NOMADBLOG_MULTIPLE_BLOGS = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)


class Blog(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogUser')
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        filters = {}
        if NOMADBLOG_MULTIPLE_BLOGS:
            filters['blog_slug'] = self.slug
        return reverse('list_posts', kwargs=filters)


class BlogUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog)
    bio = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u"%s - %s" % (self.user, self.blog)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    PUBLIC_STATUS = 0
    DRAFT_STATUS = 1
    PRIVATE_STATUS = 2
    DEFAULT_POST_STATUS_CHOICES = (
        (PUBLIC_STATUS, 'public'),
        (DRAFT_STATUS, 'draft'),
        (PRIVATE_STATUS, 'private'),
    )
    POST_STATUS_CHOICES = getattr(settings, 'POST_STATUS_CHOICES', DEFAULT_POST_STATUS_CHOICES)

    bloguser = models.ForeignKey(BlogUser)
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS_CHOICES, default=0)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category)
    content = models.TextField()

    def get_absolute_url(self):
        filters = {'category_slug': self.category.slug, 'slug': self.slug}
        if NOMADBLOG_MULTIPLE_BLOGS:
            filters['blog_slug'] = self.bloguser.blog.slug
        return reverse('show_post', kwargs=filters)

    def __unicode__(self):
        return u"%s - %s" % (self.bloguser, self.title)

    class Meta:
        abstract = True

