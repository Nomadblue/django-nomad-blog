from django.conf.urls.defaults import patterns, url
from nomadblog.views import PostList


urlpatterns = patterns('nomadblog.views',
    # List blog posts
    url('^$', PostList.as_view(), name='list_posts'),
    # Show single post, category + slug based URL
    url(
        regex=r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$',
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
        regex=r'^(?P<category>[-\w]+)/$',
        view='list_posts_by_category',
        name='list_posts_by_category',
    ),
)
