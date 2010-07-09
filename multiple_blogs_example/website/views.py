from django.shortcuts import render_to_response
from django.template import RequestContext

from nomadblog.models import Blog
from nomadblog.views import list_categories_ctxt

def home(request, template):
    """List all blogs in the site"""
    blogs = Blog.objects.all()
    return render_to_response(template, {'blogs': blogs},
        context_instance=RequestContext(request))

def list_categories_by_user(request, blog_slug, username, model, template):
    """
    This view is an example on how you can use the _ctxt functions
    in Nomadblog views to populate your template context, add any other
    stuff you'd need and finally render your response.
    """
    context = list_categories_ctxt(request, blog_slug=blog_slug,
                                   model=model, username=username)
    return render_to_response(template, {'multiblog': True}, context)
