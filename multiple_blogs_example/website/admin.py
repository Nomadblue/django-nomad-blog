from django.contrib import admin

from website.models import WebsitePost


class WebsitePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'summary')
    fields = ('bloguser', 'status', 'title', 'slug', 'category', 'summary', 'content')

admin.site.register(WebsitePost, WebsitePostAdmin)

