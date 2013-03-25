from django import template

from nomadblog.models import Category
from nomadblog.utils import get_post_model


register = template.Library()

POST_MODEL = get_post_model()

@register.assignment_tag
def get_latest_posts():
    return POST_MODEL.objects.order_by('-pub_date')

@register.assignment_tag
def get_popular_posts():
    return POST_MODEL.objects.order_by('-pub_date')

@register.assignment_tag
def get_categories():
    return Category.objects.all()

