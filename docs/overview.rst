.. _overview:

================
Django Nomadblog
================


Overview
========

This is a basic Django_ application implementing the most simplest form of a blog (from my point of view, of course). It has been written with an eye on keeping modularity as far as possible, so you won't find lots of goodies in the code, but just a couple of features to help you start hacking. 

Visit the app homepage_ for a complete detailed information.

.. _homepage: http://nomadblue.com/projects/django-nomadblog/

Features
========

 1. A mechanism to tell the application if there's gonna be only one blog or multiple blogs and users, easily configurable via a project setting and a URL pattern.
 2. Views are split into two functions, one for the view logic and the other in charge of creating or updating the ``RequestContext``. This enables calling the logic behind a view without rendering the response. It is better explained below.

.. _Django: http://www.djangoproject.com/


Installation
============

The package is listed in the `Python Package Index`_. You can use easy_install::

    sudo easy_install django_nomadblog

You can alternatively download the source code for the latest release here: http://bitbucket.org/nabucosound/django-nomadblog/downloads/

.. _Python Package Index: http://pypi.python.org/

Mercurial checkout
------------------

Install Mercurial_ if you don't have it yet, and clone the repository::

    hg clone http://bitbucket.org/nabucosound/django-nomadblog/
    
Symlink to the folder called ``nomadblog`` inside ``django-nomadblog`` from somewhere in your PYTHONPATH -- could be the system-wide ``site-packages`` python folder, or the path your virtualenv project is using, if you are using Virtualenv_ (which I strongly encourage). And if you do and are also using Virtualenvwrapper_ then you can easily ``add2virtualenv``.

.. _Mercurial: http://www.selenic.com/mercurial/
.. _Virtualenv: http://pypi.python.org/pypi/virtualenv/
.. _Virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/


Configuration
=============

Add ``nomadblog`` to the ``INSTALLED_APPS`` setting of your settings file.

Define the variable ``NOMADBLOG_SINGLE_USER`` in your project settings.py as ``True`` if you want a single blog configuration, or ``False`` if you will allow for multiple blog nesting. For example, for a single user installation, set::

    NOMADBLOG_SINGLE_USER = True

Put this code somewhere in the beggining of your root ``urls.py``::

    NOMADBLOG_SINGLE_USER = getattr(settings, 'NOMADBLOG_SINGLE_USER', False)

Include this URL pattern in your root ``urls.py``::

  (r'^blog/', include('nomadblog.urls')) if NOMADBLOG_SINGLE_USER else (r'^blogs/(?P<username>\w+)/', include('nomadblog.urls'))

You can change the ``blog/`` or ``blogs/`` part but do not modify ``(?P<username>\w+)``, because it is used in the app code.


Creating Templates
==================

``django-nomadblog`` views render four templates, one for each view (``list_posts``, ``show_post``, ``list_categories``, ``list_posts_by category``) named after its corresponding view name, plus '.html'.

If you are happy with this layout, you can just simply create a folder called ``nomadblog`` in one of your template paths (like ``yourproject/templates/nomadblog``) and include these four template files.

If you otherwise prefer any other templates, you can override the ``template`` variable each view receives by passing it through the kwargs in the URLconf::

  url(
      regex=r'^$',
      view='list_posts',
      name='list_posts',
      kwargs={'template': 'yourtemplatepath/templates/yourtemplate.html'},
  )

Introspecting ``nomadblog.views`` will give you the clue on what context each template is going to receive.


Creating custom wrappers for views
==================================

If you want to extend functionality beyond the basic logic behind a ``django-nomadblog`` view, you can call the underscored version of the view. Passing a Django ``RequestContext`` the function will update it with the expected values needed for rendering the response. If the username parameter is passed, an extra filter will be used in the Django ORM calls -- you may pass it if you are in a multiuser configuration. If you do not pass any ``RequestContext`` object, a new one is created and returned.

So, for instance, say you want to wrap around ``list_post`` view::

  from django.shortcuts import render_to_response
  from nomadblog.views import _list_posts

  def your_view(request, username=None):
      context = _list_posts(request, username=username)
      return render_to_response('your_temaplate.html', {}, context_instance=context) 


A comment on categories model
=============================

This model is included to allow one -- and only one -- category for each blog post. I could have ommited this feature and delegated it to other parts such as django-tagging_. But first, all I needed when I was writing was one category to start up the blog quickly. And second, although I always try to keep my code clean and simple, I as well fancy the "batteries-included" concept Python and Django praise. So finally I included the model in the first version of this application. I don't think it'll annoy people implementing their own category system, theirs and this can cohabit smoothly.

.. _django-tagging: http://code.google.com/p/django-tagging/

