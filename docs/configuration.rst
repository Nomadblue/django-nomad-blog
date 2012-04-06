=============
Configuration
=============

Add ``nomadblog`` to the ``INSTALLED_APPS`` setting of your ``settings.py``::

    INSTALLED_APPS = (
        ...
        'nomadblog',
    )

If you use `South`_ you can run the included migrations::

    ./manage.py migrate nomadblog

.. _`South`: http://south.aeracode.org/

If you don't, use your own migration tool or simply ``syncdb``::

    ./manage.py syncdb

Include this two lines of code in your root ``urls.py``::

    # Put it somewhere in the beginning of the file
    from django.conf import settings
    MULTIBLOG = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)
    
    # Add this pattern into your url conf
    urlpatterns = patterns('',
        ...
        url(r'^blog/', include('nomadblog.urls')) if not MULTIBLOG \
            else (r'^blogs/(?P<blog_slug>[-\w]+)/', include('nomadblog.urls')),
    )

You can change the ``blog/`` or ``blogs/`` initial part but do not modify
``(?P<blog_slug>\w+)``, because it is used by the app to differenciate which
blog is being accessed, in case multiblog is used.

Settings
========

Multiblog
---------

Define the variable ``NOMADBLOG_MULTIPLE_BLOGS`` in your project settings
as ``True`` if you want a multiple blog configuration::

    NOMADBLOG_MULTIPLE_BLOGS = True

Default Post model
------------------

By default, ``django-nomadblog`` uses the ``Post`` model, but you can extend it
with your own one, that will be then used by the app views::

    POST_MODEL = 'yourapp.models.YourExtendedPostModel'

