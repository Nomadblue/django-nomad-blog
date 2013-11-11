=============
Configuration
=============

Multiblog
=========

A simple project setting and a URL pattern is all we need to configure our
django-omadblog installation for single or multiple blog management.

If you want to maintain multiple blogs, enable the following variable in
your project settings::

    NOMADBLOG_MULTIPLE_BLOGS = True

Multiblog-enabled configurations require that the urls receive the ``blog_slug``::

    # Add this pattern into your root url conf
    urlpatterns = patterns('',
        ...
        (r'^blogs/(?P<blog_slug>[-\w]+)/', include('nomadblog.urls')),

Otherwise just do::

    (r'^blog', include('nomadblog.urls')),

Default Post model
==================

By default, ``django-nomadblog`` uses the ``Post`` model, but you can extend it
with your own one, that will be then used by the app views::

    POST_MODEL = 'yourapp.models.YourExtendedPostModel'

Post status' choices
====================

By default posts can be draft, private or public, only public ones are listed
or displayed.  You can override your status choices as well as which one of
the choices is the display filter for listings::

    POST_STATUS_CHOICES = (
        (0, 'Borrador'),
        (1, 'Pendiente de revision'),
        (2, 'Revisado'),
        (3, 'Publicado'),
    )
    PUBLIC_STATUS = 3
