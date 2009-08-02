from django.contrib import admin

from nomadblog.models import Post, Blog, Category

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Post)
