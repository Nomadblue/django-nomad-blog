Installation
============

The package is listed in the `Python Package Index`_. You can use your
favorite package manager like easy_install or pip::

    pip install django_nomadblog

You can also download the source code for the latest release or
development version here::

    http://bitbucket.org/nabucosound/django-nomadblog/downloads/

.. _Python Package Index: http://pypi.python.org/pypi/django-nomadblog/

Mercurial checkout
------------------

Install Mercurial_ if you don't have it yet, and clone the repository::

    hg clone http://bitbucket.org/nabucosound/django-nomadblog/
    
For the old-school guys, symlink to the folder called ``nomadblog`` inside
``django-nomadblog`` from somewhere in your PYTHONPATH -- could be the
system-wide ``site-packages`` python folder, or the path your Virtualenv_
project is using, if you are using it (which I strongly encourage). And if you
do and are also using Virtualenvwrapper_ then you can easily ``add2virtualenv``.

.. _Mercurial: http://www.selenic.com/mercurial/
.. _Virtualenv: http://pypi.python.org/pypi/virtualenv/
.. _Virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/

Configuration
=============

Add ``nomadblog`` to the ``INSTALLED_APPS`` setting of your ``settings.py``::

    INSTALLED_APPS = (
        ...
        'nomadblog',
    )

``django-nomadblog`` comes with migrations for the South_ tool::

    ./manage.py migrate nomadblog

If you don't use migrations (you should!) or use a different way to update
your database,  use ``syncdb``::

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

Overrriding templates
=====================

``django-nomadblog`` uses different templates to list posts, show a post details,
list categories or list posts by categary. You will want to override these
templates, to add your layout, design and own stuff. Create a new ``nomadblog``
template folder where your project can find it and copy the templates found on
the ``templates/nomadblog`` directory (like ``list_posts.html`` or
``show_post.html``) or, if you want to be quicker, just copy the entire
``templates/nomadblog`` folder.

