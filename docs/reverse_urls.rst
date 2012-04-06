============
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

