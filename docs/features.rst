========
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
* **Complete example projects**: As usual with my open sourced Django projects,
  I include two example project folders, one for a single blog installation
  (``single_blog_example``) and another one for multiblog
  (``multiple_blogs_example``), where you can see all the things explained
  here in practice.

.. _`Custom view wrappers`: custom_view_wrappers
