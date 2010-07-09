from django.shortcuts import render_to_response
from django.template import RequestContext

from nomadblog.views import list_categories_ctxt

def home(request, template):
    """
    This view is an example on how you can use the _ctxt functions
    in Nomadblog views to populate your template context, add any other
    stuff you'd need and finally render your response.
    """
    context = list_categories_ctxt(request, blog_slug='hector-blog',
                                   username='hector')
    return render_to_response(template, context_instance=context)
