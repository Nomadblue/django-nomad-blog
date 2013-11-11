from django.conf.urls import patterns, url
from nomadblog.views import PostList, PostDetail


urlpatterns = patterns(
    'nomadblog.views',
    url(r'^$', PostList.as_view(), name='list_posts'),
    url('^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='show_post'),
    url(regex=r'^categories/list/all/$', view='list_categories', name='list_categories'),
    url(regex=r'^(?P<category>[-\w]+)/$', view='list_posts_by_category', name='list_posts_by_category'),
)
