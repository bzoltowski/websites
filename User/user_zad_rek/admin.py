from django.contrib import admin

# Register your models here.
from .models import WebsiteCategory, Website, WebPage

admin.site.register(Website)
admin.site.register(WebPage)
admin.site.register(WebsiteCategory)