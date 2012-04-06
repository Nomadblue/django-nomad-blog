====================
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

