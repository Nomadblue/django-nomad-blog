============
Installation
============

The package is listed in the `Python Package Index`_. You can use your favorite
package manager like ``easy_install`` or ``pip``::

    pip install django-nomadblog

Or, you can clone the latest development code from its repository::

    git clone git@github.com:nabucosound/django-nomadblog.git

.. _Python Package Index: http://pypi.python.org/pypi/django-nomadblog/

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
