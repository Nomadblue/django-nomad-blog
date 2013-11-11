from django.conf.urls import patterns, url
from nomadblog.views import PostList, PostDetail, PostsByCategoryList, CategoriesList


urlpatterns = patterns(
    'nomadblog.views',
    url(r'^$', PostList.as_view(), name='list_posts'),
    url('^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='show_post'),
    url(r'^(?P<category_slug>[-\w]+)/$', PostsByCategoryList.as_view(), name='list_posts_by_category'),
    url(r'^categories/list/all/$', CategoriesList.as_view(), name='list_categories'),
)
