=========
CHANGELOG
=========

Version 2.0.0
=============

* Remove example projects, templatetags.
* Reset south migrations and fix django custom user issues (see
  http://kevindias.com/writing/django-custom-user-models-south-and-reusable-apps/).

Version 1.1.1
=============

* Update to Django 1.6 compatibility

Version 0.4
===========

* Multiblog support
* ``BlogUser`` acts as intermediate model between ``Post`` and ``Blog``.
  A blog can belong to many blogusers.
* Settings parameter has changed from NOMADBLOG_SINGLE_USER to
  NOMADBLOG_MULTIPLE_USER.
* Post status choices can be user customized.
* Context _ctxt functions receive more parameters to allow flexibility.
* Two example projects, both for a single blogging installation and
  another one for multiple blogging, are provided to see a real
  implementation of the various methods and techniques described in
  the documentation.
* Default templates facilitate initial integration of the app
  into projects.

Nomadblog v0.3
==============

* First release
