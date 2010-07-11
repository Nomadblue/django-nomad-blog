================
Django Nomadblog
================

This is the documenation for django-nomadblog v0.4. To see docs for
former releases, please check out the ``docs/`` folder in the
sorce code distribution package corresponding to your version.

Overview
========

This is a basic Django_ application implementing the simplest form of a
blogging system. It's able to handle multible blogs and users.
It has been written with an eye put on keeping modularity and flexibility as
much as possible, so you won't find lots of goodies in the code (tagging,
related posts, blogroll), but just a couple of features to help you start
hacking it to your needs.

Visit the project homepage_ or read the documentation files found in the
``docs/`` folder for a complete detailed information.

.. _Django: http://www.djangoproject.com/
.. _homepage: http://nomadblue.com/projects/django-nomadblog/

Features
========

* **Multiblog**: A simple project setting and a URL pattern is all we need to
  configure our Nomadblog installation for single or multiple blog management.
* **Multiuser**: The application allows one or many authors writing content
  to the same blog.
* **Simplicity and flexibility**: A post can have a category and an status
  assigned. That's it. Everything else is up to you and you will have to code it
  yourself, which means you control what is in your project, how it works, etc.
* **Context update functions**: Default Nomadblog views are only a thin wrapper
  that call their respective ``_ctxt`` related functions (which have the
  business logic) and return the response. The use of this mechanism is better
  explained in the section `Custom view wrappers`_.
* **Complete example projects**: As usual with my open sourced Django projects_,
  I include two example project folders, one for a single blog installation
  (``single_blog_example``) and another one for multiblog
  (``multiple_blogs_example``), where you can see all the things explained
  here in practice.

.. _projects: http://nomadblue.com/projects/

Installation
============

The package is listed in the `Python Package Index`_. You can use your
favorite package manager like easy_install or pip::

    pip install django_nomadblog

You can alternatively download the source code for the latest release or
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

Add ``nomadblog`` to the ``INSTALLED_APPS`` setting of your settings file,
and ``syncdb`` your database if you need to::

	INSTALLED_APPS = (
		...
		'nomadblog',
	)

Include this two lines of code in your root ``urls.py``::

	# Put it somewhere in the beginning of the file
	NOMADBLOG_MULTIPLE_BLOGS = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)
	
	# Add this pattern into your url conf
	urlpatterns = patterns('',
		...
	    (r'^blog/', include('nomadblog.urls')) if not NOMADBLOG_MULTIPLE_BLOGS \
            else (r'^blogs/(?P<blog_slug>[-\w]+)/', include('nomadblog.urls')),
	)

You can change the ``blog/`` or ``blogs/`` initial part but do not modify
``(?P<blog_slug>\w+)``, because it is used by the app to differenciate which
blog is being accessed, in case multiblog is used.

Setting multiblog
=================

Define the variable ``NOMADBLOG_MULTIPLE_BLOGS`` in your project settings.py
as ``True`` if you want a Multiple blog configuration::

    NOMADBLOG_MULTIPLE_BLOGS = True

Blog users
==========

Blog users are Django users — from ``django.contrib.auth`` — related to a
``Blog`` model instance. Each post is owned by a ``BlogUser`` which, in turn,
belongs to a ``Blog``.

Passing view parameters
=======================

Views receive a number of parameters that are used to specify, change or
override different parts of the app. If you take a look at the Nomadblog
default views you will see how flexible Nomadblog is intended to be.

In order to pass parameters to Nomadblog views, you must first of all create
a copy of the ``urls.py`` file in the Nomadblog app::

	cp [path to nomadblog app]/urls.py yourproject/yourapp/blog_urls.py

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

Overriding templates
====================

``django-nomadblog`` comes with four templates, one for each view
(``list_posts``, ``show_post``, ``list_categories``, ``list_posts_by category``)
named after its corresponding view name, plus '.html'.

If you are happy with this layout, you can create a folder called ``nomadblog``
in one of your template paths (like ``yourproject/templates/nomadblog``) and
include these four template files to modify them, or just simply leave them in
their original Nomadblog folder (barebone templates, though).

If you otherwise want to specify your own template for a view, you can
override the ``template`` variable the view receives by passing it
through the kwargs in the URLconf::

	url(
		regex=r'^$',
	    view='list_posts',
	    name='list_posts',
	    kwargs={'template': 'yourtemplatepath/templates/yourtemplate.html'},
	)

Custom view wrappers
====================

If you want to extend functionality beyond the basic logic behind a Nomadblog
view, you can call, from your wrapper view function, one of the ``_ctxt``
functions defined in ``views.py`` directly with your context. Passing a
``RequestContext`` to the function will update it with the expected values
needed for rendering the response. If you do not pass any ``RequestContext``
object, a new one is created and returned.

Basically the idea behind having the business logic separated from template
context population is that you can have the basic functionality of the action
performed in the blog (get a list of posts, show the contents of a post)
isolated and DRY, and add or modify business logic to your wrapper view.

I wrote a post_ trying to explain better this approach. Also, the four
Nomadblog actions represented by their four view functions — ``list posts``,
``show post``, ``list categories``, ``show post by category`` — in the
``views.py`` code are actually the best examples to implement your own wrapper.

.. _post: http://nomadblue.com/blog/django/context-in-django-views-dry-reusable-apps/

Post model subclassing
======================

The ``Post`` model contains a small set of fields, which provide just the
basics for a blog application. You may want to extend it, just subclass it.
For example, in nomadblog.com I have a ``summary`` field that shows an excerpt
of the post when listing latest posts::

	from nomadblog.models import Post
	
	class NomadbluePost(Post):
	    summary = tinymce_models.HTMLField()

In order to use your model instead of the default ``Post`` in the Nuvolic
views, pass the model through the ``kwargs`` in the URL conf (see
`Overriding templates`_ for another example)::

	from nomadblue.models import NomadbluePost
	
	url(
		regex=r'^$',
	    view='list_posts',
	    name='list_posts',
	    kwargs={'model': NomadbluePost},
	)

Custom status choices
=====================

If you want to use your own set of status choices — used by the ``status``
field in the ``Post`` model — you must define it in your settings::

	PUBLIC_STATUS = 0
	MY_STATUS = 1
	MY_OTHER_STATUS = 2
	POST_STATUS_CHOICES = (
		(PUBLIC_STATUS, 'public status'),
		(MY_STATUS, 'my status'),
		(MY_OTHER_STATUS, 'my other status'),
	)

You must mantain at least ``PUBLIC_STATUS = 0`` because it is used as default
value for both ``status`` field in the ``Post`` model  and the Nomadblog views.

Reverse urls
============

Reverse URLs in templates will vary depending on your multiblog configuration.
Nomadblog views add a ``multiblog`` flag in the context to use the right
``url`` template tag parameters. Take, for instance, this sampe code from
``show_post.html``::

	{% if multiblog %}
	<a href="{% url list_posts_by_category
        bloguser.blog.slug post.category.name %}" class="link-categories">
        {{ post.category.name }}</a>
	{% else %}
	<a href="{% url list_posts_by_category post.category.name %}"
        class="link-categories">{{ post.category.name }}</a>
	{% endif %}

You probably won't need this if you are using your own templates, because
you will set up your templates in advance.
