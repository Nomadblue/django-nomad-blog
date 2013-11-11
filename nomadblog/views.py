from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response
from django.template import RequestContext
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


class PostList(ListView):
    model = POST_MODEL
    template_name = 'nomadblog/list_posts.html'

    def get_queryset(self, *args, **kwargs):
        """Extra kwargs may be passed using the urlpattern definitions"""
        extra_filters = _get_extra_filters(self.kwargs)
        return self.model.objects.filter(**extra_filters)


class PostDetail(DetailView):
    model = POST_MODEL
    template_name = 'nomadblog/show_post.html'

    def get_queryset(self, *args, **kwargs):
        """Extra kwargs may be passed using the urlpattern definitions"""
        extra_filters = _get_extra_filters(self.kwargs)
        extra_filters['category'] = get_object_or_404(Category, slug=self.kwargs.get('category_slug', ''))
        return self.model.objects.filter(**extra_filters)


def list_categories_ctxt(request, context=None, model=POST_MODEL,
                         blog_slug=None, username=None, status=None):
    """
    Returns a list of categories. ``model`` param specifies post Model to
    retrieve, either ``Post`` model by default or
    a subcclass defined by the user. ``blog_slug`` and ``status``
    may be included as extra filters in the query, if passed.
    If no ``context`` is passed, it returns the results in a new
    ``RequestContext`` instead of updating the given one.
    """
    extra_filters = _get_extra_filters(blog_slug, username, status)
    posts = model.objects.filter(**extra_filters)
    cat_ids = posts.values_list('category', flat=True)
    categories = Category.objects.filter(id__in=cat_ids)
    ctxt_dict = {'categories': categories}
    ctxt_dict.update(**extra_filters)
    return RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)


def list_posts_by_category_ctxt(request, category_slug, context=None, model=POST_MODEL,
                                blog_slug=None, username=None, status=None):
    """
    Returns a list of posts related to a given category. ``model`` param
    specifies post Model to retrieve, either ``Post`` model by default or
    a subcclass defined by the user. ``blog_slug`` and ``status``
    may be included as extra filters in the query, if passed.
    If no ``context`` is passed, it returns the results in a new
    ``RequestContext`` instead of updating the given one.
    """
    extra_filters = _get_extra_filters(blog_slug, username, status)
    cat = get_object_or_404(Category, slug=category_slug)
    posts = model.objects.filter(category=cat, **extra_filters)
    ctxt_dict = {'posts': posts, 'category': cat}
    ctxt_dict.update(**extra_filters)
    return RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)


# You can use these following views as examples of how to use the _ctxt
# functions above and get more flexibility, or you can simply use them
# directly as views into your project.

def list_categories(request, model=POST_MODEL, blog_slug=None,
                    username=None, status=DEFAULT_STATUS,
                    extra_ctxt={}, template='nomadblog/list_categories.html'):
    """
    By default, a queryset of categories related to published Post model
    instances for all users are retrieved.
    You can override these settings if you want to.
    """
    context = list_categories_ctxt(request, blog_slug=blog_slug,
                                   username=username)
    context.update(extra_ctxt)
    return render_to_response(template, {'multiblog': multiblog}, context)


def list_posts_by_category(request, category, model=POST_MODEL,
                           blog_slug=None, username=None,
                           status=DEFAULT_STATUS, order='-pub_date',
                           extra_ctxt={},
                           template='nomadblog/list_posts_by_category.html'):
    """
    By default, a queryset of published Post model
    instances related to the given category and for all users are retrieved.
    You can override these settings if you want to.
    """
    context = list_posts_by_category_ctxt(request, category, model=model,
                                          username=username,
                                          blog_slug=blog_slug)
    context['posts'] = context['posts'].order_by(order)
    context.update(extra_ctxt)
    return render_to_response(template, {'multiblog': multiblog}, context)
