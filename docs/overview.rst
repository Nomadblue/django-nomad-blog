.. _overview:

================
Django Nomadblog
================


Overview
========

This is a basic Django_ application implementing the most simplest form of a blog. It has been written with an eye on keeping modularity as far as possible. That means trying to keep users away from tweaking things right from the start. django-nomadblog has a mechanism to tell the application if there's gonna be only one blog or multiple blogs and users.

.. _Django: http://www.djangoproject.com/


Installation
============

Soon I'll package the whole thing and upload it to PyPi_ for the sake of standard installations.

.. _Pypi: http://pypi.python.org/

Mercurial checkout
------------------

Install Mercurial_ if you don't have it yet, and clone the repository::

    hg clone http://bitbucket.org/nabucosound/django-nomadblog/
    
Symlink to the folder called ``nomadblog`` inside ``django-nomadblog`` from somewhere in your PYTHONPATH -- could be the system-wide ``site-packages`` python folder, or the path your virtualenv project is using, if you are using Virtualenv_ (which I strongly encourage).

.. _Mercurial: http://www.selenic.com/mercurial/
.. _Virtualenv: http://pypi.python.org/pypi/virtualenv/


Configuration
=============

Add ``nomadblog`` to the ``INSTALLED_APPS`` setting of your settings file.

Define the variable ``NOMADBLOG_SINGLE_USER`` in your project settings.py as ``True`` if you want a single blog configuration, or ``False`` if you will allow for multiple blog nesting. For example::

    NOMADBLOG_SINGLE_USER = True

Put this code somewhere in the beggining of your root ``urls.py``::

  try:
      from settings import NOMADBLOG_SINGLE_USER
  except ImportError:
      NOMADBLOG_SINGLE_USER = False

Include this URL pattern also in urlpatterns in your root ``urls.py``::

  (r'^blog/', include('nomadblog.urls')) if NOMADBLOG_SINGLE_USER else (r'^blogs/(?P<username>\w+)/', include('nomadblog.urls'))


Creating Templates
==================

django-nomadblog views render four templates, one for each view (list posts, view post, list categories, list posts by category): ``nomadblog/list_posts.html``, ``nomadblog/show_post.html``, ``nomadblog/list_categories.html``, and ``nomadblog/list_posts_by_category.html``.

If you are happy with this layout, you can just simply create a folder called ``nomadblog`` in one of your template paths (like ``yourproject/templates/nomadblog``) and include these four template files.

If you otherwise prefer any other setting, you can override the ``template`` variable each view receives by passing it through the kwargs in the URLconf::

  url(
      regex=r'^$',
      view='list_posts',
      name='list_posts',
      kwargs={'template': 'yourtemplatepath/yourtemplate.html'},
  )


A comment on categories
=======================

This model is included to allow one -- and only one -- category for each blog post. I could have ommited this feature and delegated it to other parts such as django-tagging_. But first, all I needed when I was writing was one category to start up the blog quickly. And second, although I always try to keep my code clean and simple, I as well fancy the "batteries-included" concept Python and Django praise. So finally I included the model in the first version of this application for the sake of the former statements. I don't think it'll annoy people implementing their own category system, theirs and this can cohabit smoothly.

.. _django-tagging: http://code.google.com/p/django-tagging/

