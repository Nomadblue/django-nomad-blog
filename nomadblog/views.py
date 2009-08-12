from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from nomadblog.models import Post, Category


def _get_extra_filters(username=None):
    """
    Set a queryset param to filter by blog, if username is
    provided -- that is, Nomadblog is being used in a multi-user layout.
    """
    extra_filters = {}
    if username is not None:
        u = get_object_or_404(User, username=username)
        extra_filters['blog__user'] = u
    return extra_filters

def _list_posts(request, context=None, username=None):
    """Populates context with values required by list_posts view"""
    extra_filters = _get_extra_filters(username)
    posts = Post.objects.filter(status=Post.PUBLIC_STATUS,\
        **extra_filters).order_by('-pub_date')
    ctxt_dict = {'posts': posts}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    return context

def _show_post(request, category, slug, context=None, username=None):
    extra_filters = _get_extra_filters(username)
    cat = get_object_or_404(Category, name=category)
    post = get_object_or_404(Post, category=cat, slug=slug,
                             status=Post.PUBLIC_STATUS, **extra_filters)
    ctxt_dict = {'post': post}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    return context

def _list_categories(request, context=None, username=None):
    categories = Category.objects.all() # TODO: only cats from username
    ctxt_dict = {'categories': categories}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    return context

def _list_posts_by_category(request, category, context=None, username=None):
    extra_filters = _get_extra_filters(username)
    cat = get_object_or_404(Category, name=category)
    posts = Post.objects.filter(category=cat, status=Post.PUBLIC_STATUS, \
        **extra_filters).order_by('-pub_date')
    ctxt_dict = {'posts': posts, 'category': category}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    return context

def list_posts(request, username=None, template='nomadblog/list_posts.html'):
    """A list of posts, orderen in reverse chronological order."""
    context = _list_posts(request, username=username)
    return render_to_response(template, {}, context)

def show_post(request, category, slug, username=None,
              template='nomadblog/show_post.html'):
    context = _show_post(request, category, slug, username=username)
    return render_to_response(template, {}, context)

def list_categories(request, username=None,
                    template='nomadblog/list_categories.html'):
    context = _list_categories(request, username=username)
    return render_to_response(template, {}, context)

def list_posts_by_category(request, category,
                           username=None, render_response=True, context=None,
                           template='nomadblog/list_posts_by_category.html'):
    context = _list_posts_by_category(request, category, username=username)
    return render_to_response(template, {}, context)

