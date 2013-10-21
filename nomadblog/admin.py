from django.contrib import admin

from nomadblog.models import Blog, Category, BlogUser

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(BlogUser)
