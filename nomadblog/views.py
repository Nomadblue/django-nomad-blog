from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from nomadblog.models import Post, Category


def _get_extra_filters(username=None):
    extra_filters = {}
    if username is not None:
        u = get_object_or_404(User, username=username)
        extra_filters['blog__user'] = u
    return extra_filters

def show_post(request, category, slug, username=None, render_response=True,
              context=None, template='nomadblog/show_post.html'):
    extra_filters = _get_extra_filters(username)
    try:
        cat = Category.objects.get(name=category)
        post = Post.objects.get(category=cat, slug=slug,
                                status=Post.PUBLIC_STATUS, **extra_filters)
    except ObjectDoesNotExist:
        raise Http404
    ctxt_dict = {'post': post}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    if not render_response:
        return context
    return render_to_response(template, {}, context_instance=context)

def list_posts(request, username=None, render_response=True, context=None,
               template='nomadblog/list_posts.html'):
    extra_filters = _get_extra_filters(username)
    posts = Post.objects.filter(status=Post.PUBLIC_STATUS,\
        **extra_filters).order_by('-pub_date')
    ctxt_dict = {'posts': posts}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    if not render_response:
        return context
    return render_to_response(template, {}, context_instance=context)

def list_categories(request, username=None, render_response=True, context=None,
                    template='nomadblog/list_categories.html'):
    categories = Category.objects.all()
    ctxt_dict = {'categories': categories}
    context = RequestContext(request, ctxt_dict) if context is None \
        else context.update(ctxt_dict)
    if not render_response:
        return context
    return render_to_response(template, {}, context_instance=context)

def list_posts_by_category(request, category,
                           username=None, render_response=True, context=None,
                           template='nomadblog/list_posts_by_category.html'):
    extra_filters = _get_extra_filters(username)
    cat = get_object_or_404(Category, name=category)
    posts = Post.objects.filter(category=cat, status=Post.PUBLIC_STATUS, \
        **extra_filters).order_by('-pub_date')
    return render_to_response(template, {'posts': posts, 'category': cat.name},
        context_instance=RequestContext(request))

