from django.conf.urls.defaults import *

urlpatterns = patterns('website.views',
    url(
        regex=r'^$',
        view='home',
        name='home',
        kwargs={'template': 'website/home.html'},
    ),
)
