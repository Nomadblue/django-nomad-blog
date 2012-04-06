===========================
Passing parameters to views
===========================

Views receive a number of parameters that are used to specify, change or
override different parts of the app. If you take a look at the Nomadblog
default views you will see how flexible Nomadblog is intended to be.

In order to pass parameters to Nomadblog views, you must first of all create
a copy of the ``urls.py`` file in the Nomadblog app::

    cp /path/to/django-nomadblog/urls.py /path/to/project/yourapp/blog_urls.py

Then point to it changing your project root URL pattern::

    urlpatterns = patterns('',
            ...
        (r'^blog/', include('yourapp.blog_urls')) if not \
        NOMADBLOG_MULTIPLE_BLOGS else (r'^blogs/(?P<blog_slug>\w+)/', \
        include('yourapp.blog_urls')),
    )

You can now modify your urlconf, like passing parameters to view functions
with the ``kwargs``. See the ``website/blog_urls.py`` file in the example
projects to check out a few examples.

