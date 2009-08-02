from django.conf.urls.defaults import *


urlpatterns = patterns('nomadblog.views',
    # List blog posts
    url(
        regex=r'^$',
        view='list_posts',
        name='list_posts',
    ),
    # Show single post, category + slug based URL
    url(
        regex=r'^(?P<category>\w+)/(?P<slug>[-\w]+)/$',
        view='show_post',
        name='show_post',
    ),
    # List categories
    url(
        regex=r'^categories/$',
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
