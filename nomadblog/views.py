from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.conf import settings

from nomadblog.models import Blog, BlogUser, Category
from nomadblog.utils import get_post_model


multiblog = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)
DEFAULT_STATUS = getattr(settings, 'PUBLIC_STATUS', 0)
POST_MODEL = get_post_model()


def _get_extra_filters(kwargs):
    """
    If nomadblog is being used in a multi-blog layout (NOMADBLOG_MULTIPLE_BLOGS
    setting is set to True) then ``blog_slug`` may be passed in order to filter
    posts related to blog instance only. If username and/or status are received,
    only posts written by user and/or with that status (e.g. PUBLIC_STATUS in
    Post model), respectively, will be retrieved.
    """
    extra_filters = {'status': kwargs.get('status', DEFAULT_STATUS)}
    if kwargs.get('blog_slug', None):
        blog = get_object_or_404(Blog, slug=kwargs.get('blog_slug'))
        extra_filters['bloguser__blog'] = blog
    if kwargs.get('username', None):
        bloguser = get_object_or_404(BlogUser, user__username=kwargs.get('username'))
        extra_filters['bloguser'] = bloguser
    return extra_filters


class MultiblogMixin(object):

    def get_context_data(self, *args, **kwargs):
        """Sometimes we need to know if we nomadblog is multiblog enabled"""
        context = super(MultiblogMixin, self).get_context_data(*args, **kwargs)
        context['multiblog'] = multiblog
        if multiblog:
            context['blog'] = get_object_or_404(Blog, slug=self.kwargs.get('blog_slug', ''))
        return context


class PostList(MultiblogMixin, ListView):
    model = POST_MODEL
    template_name = 'nomadblog/list_posts.html'

    def get_queryset(self, *args, **kwargs):
        """Extra kwargs may be passed using the urlpattern definitions"""
        extra_filters = _get_extra_filters(self.kwargs)
        return self.model.objects.filter(**extra_filters)


class PostDetail(MultiblogMixin, DetailView):
    model = POST_MODEL
    template_name = 'nomadblog/show_post.html'

    def get_queryset(self, *args, **kwargs):
        """Extra kwargs may be passed using the urlpattern definitions"""
        extra_filters = _get_extra_filters(self.kwargs)
        extra_filters['category'] = get_object_or_404(Category, slug=self.kwargs.get('category_slug', ''))
        return self.model.objects.filter(**extra_filters)


class PostsByCategoryList(MultiblogMixin, ListView):
    model = POST_MODEL
    template_name = 'nomadblog/list_posts_by_category.html'

    def get_queryset(self, *args, **kwargs):
        """Extra kwargs may be passed using the urlpattern definitions"""
        extra_filters = _get_extra_filters(self.kwargs)
        self.category = get_object_or_404(Category, slug=self.kwargs.get('category_slug', ''))
        extra_filters['category'] = self.category
        return self.model.objects.filter(**extra_filters).order_by('-pub_date')

    def get_context_data(self, *args, **kwargs):
        context = super(PostsByCategoryList, self).get_context_data(*args, **kwargs)
        context['category'] = self.category
        return context


class CategoriesList(MultiblogMixin, ListView):
    model = Category
    template_name = 'nomadblog/list_categories.html'
