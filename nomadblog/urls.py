from django.conf.urls import patterns, include, url
from nomadblog.views import PostList


urlpatterns = patterns(
    'nomadblog.views',
    url('^$', PostList.as_view(), name='list_posts'),
    url(regex=r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', view='show_post', name='show_post'),
    url(regex=r'^categories/list/all/$', view='list_categories', name='list_categories'),
    url(regex=r'^(?P<category>[-\w]+)/$', view='list_posts_by_category', name='list_posts_by_category'),
)
