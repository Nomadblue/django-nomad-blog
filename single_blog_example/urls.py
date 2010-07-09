import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

# Check out if multiblog is being used
NOMADBLOG_MULTIPLE_BLOGS = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)

admin.autodiscover()

urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    # Nomadblog urls
    (r'^blog/', include('nomadblog.urls')) if not NOMADBLOG_MULTIPLE_BLOGS \
        else (r'^blogs/(?P<blog_slug>[-\w]+)/', include('nomadblog.urls')),
    # Website app is used to add a view to render homepage
    (r'^$', include('website.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(
            regex=r'^media/(?P<path>.*)$',
            view='django.views.static.serve',
            kwargs={'document_root': os.path.join(os.path.dirname(__file__),
                    "media")},
        )
    )

