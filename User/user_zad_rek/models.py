from django.db import models

# Create your models here.

class WebsiteCategory(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    count = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

class Website(models.Model):
    url = models.CharField(max_length=256, unique=True)
    title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(WebsiteCategory, null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

class WebPage(models.Model):
    website = models.ForeignKey(Website, null=True, blank=True, on_delete=models.CASCADE)
    URL = models.CharField(max_length=256, unique=True)
    title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
