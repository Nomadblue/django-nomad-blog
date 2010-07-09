from django.conf.urls.defaults import *

from website.models import WebsitePost


urlpatterns = patterns('nomadblog.views',
    # List blog posts
    # Our WebsitePost model, subclassing nomadblog Post, is used
    # We are passing an specified ordering here as well.
    url(
        regex=r'^$',
        view='list_posts',
        name='list_posts',
        kwargs={'model': WebsitePost, 'order': 'pub_date'},
    ),
    # Show single post, category + slug based URL
    url(
        regex=r'^(?P<category>\w+)/(?P<slug>[-\w]+)/$',
        view='show_post',
        name='show_post',
    ),
    # List categories
    url(
        regex=r'^categories/list/all/$',
        view='list_categories',
        name='list_categories',
    ),
    # List posts by category
    url(
        regex=r'^(?P<category>\w+)/$',
        view='list_posts_by_category',
        name='list_posts_by_category',
    ),
)

urlpatterns += patterns('website.views',
    # List categories for a given user
    url(
        regex=r'^categories/(?P<username>\w+)/list/$',
        view='list_categories_by_user',
        name='list_categories_by_user',
        kwargs={'model': WebsitePost,
                'template': 'nomadblog/list_categories.html'},
    ),

)
