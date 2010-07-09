from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

import settings
from nomadblog.models import Blog, BlogUser, Post, Category

multiblog = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False) 
DEFAULT_STATUS = getattr(settings, 'PUBLIC_STATUS', 0)


def _get_extra_filters(blog_slug=None, username=None, status=None):
    """
    If nomadblog is being used in a multi-blog layout (NOMADBLOG_MULTIPLE_BLOGS
    setting is set to True) then ``blog_slug`` may be passed in order to filter
    posts related to blog instance only. If username and/or status are received,
    only posts written by user and/or with that status (e.g. PUBLIC_STATUS in
    Post model), respectively, will be retrieved.
    """
    extra_filters = {}
    if blog_slug is not None:
        blog = get_object_or_404(Blog, slug=blog_slug)
        extra_filters['bloguser__blog'] = blog
    if username is not None:
        bloguser = get_object_or_404(BlogUser, user__username=username)
        extra_filters['bloguser'] = bloguser
    if status is not None:
        extra_filters['status'] = status
    return extra_filters

def list_posts_ctxt(request, context=None, model=Post,
                    blog_slug=None, username=None, status=None):
    """
    Returns a queryset of post instances. ``model`` param specifies
    post Model to retrieve, either ``Post`` model by default or
    a subcclass defined by the user. ``blog_slug`` and ``status``
    may be included as extra filters in the query, if passed.
    If no ``context`` is passed, it returns the results in a new
    ``RequestContext`` instead of updating the given one.
    """
    extra_filters = _get_extra_filters(blog_slug, username, status)
    posts = model.objects.filter(**extra_filters)
    ctxt_dict = {'posts': posts}
    ctxt_dict.update(**extra_filters)
    return RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)

def show_post_ctxt(request, category, slug, context=None, model=Post,
                   blog_slug=None, username=None, status=None):
    """
    Returns a post instance with given ``slug``, related to category. ``model``
    param specifies post Model to retrieve, either ``Post`` model by default or
    a subcclass defined by the user. ``blog_slug`` and ``status``
    may be included as extra filters in the query, if passed.
    If no ``context`` is passed, it returns the results in a new
    ``RequestContext`` instead of updating the given one.
    """
    extra_filters = _get_extra_filters(blog_slug, username, status)
    cat = get_object_or_404(Category, name=category)
    post = get_object_or_404(model, category=cat, slug=slug, **extra_filters)
    ctxt_dict = {'post': post}
    ctxt_dict.update(**extra_filters)
    return RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)

def list_categories_ctxt(request, context=None, model=Post,
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

def list_posts_by_category_ctxt(request, category, context=None, model=Post, 
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
    cat = get_object_or_404(Category, name=category)
    posts = model.objects.filter(category=cat, **extra_filters)
    ctxt_dict = {'posts': posts, 'category': category}
    ctxt_dict.update(**extra_filters)
    return RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)

# You can use these following views as examples of how to use the _ctxt
# functions above and get more flexibility, or you can simply use them
# directly as views into your project.

def list_posts(request, model=Post, blog_slug=None, username=None,
               status=DEFAULT_STATUS, order='-pub_date',
               template='nomadblog/list_posts.html'):
    """
    By default, a queryset of published Post model instances for all users
    are retrieved, ordered in reverse chronological order.
    You can override these settings if you want to.
    """
    context = list_posts_ctxt(request, model=model, blog_slug=blog_slug,
                              username=username, status=status)
    context['posts'] = context['posts'].order_by(order)
    return render_to_response(template, {'multiblog': multiblog}, context)

def show_post(request, category, slug, model=Post, blog_slug=None,
              username=None, status=DEFAULT_STATUS,
              template='nomadblog/show_post.html'):
    """
    By default, a published Post model instance for a given user is retrieved.
    You can override these settings if you want to.
    """
    context = show_post_ctxt(request, category, slug, model=model,
                             username=username, blog_slug=blog_slug,
                             status=status)
    return render_to_response(template, {'multiblog': multiblog}, context)

def list_categories(request, model=Post, blog_slug=None,
                    username=None, status=DEFAULT_STATUS,
                    template='nomadblog/list_categories.html'):
    """
    By default, a queryset of categories related to published Post model
    instances for all users are retrieved.
    You can override these settings if you want to.
    """
    context = list_categories_ctxt(request, blog_slug=blog_slug,
                                   username=username)
    return render_to_response(template, {'multiblog': multiblog}, context)

def list_posts_by_category(request, category, model=Post,
                           blog_slug=None, username=None,
                           status=DEFAULT_STATUS, order='-pub_date',
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
    return render_to_response(template, {'multiblog': multiblog}, context)

