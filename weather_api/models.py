from django.db import models
from .admin import *


class Suscribe(models.Model):
    email = models.EmailField(max_length=30)




# Create your models here.

# class Social(models.Model):
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     github_url = models.CharField(max_length=255, null=True, blank=True)
#     linkedin_url = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.website_url



class mnews(models.Model):
    nhead = models.CharField(max_length=100)
    ntitle = models.CharField(max_length=100)
    ncity = models.CharField(max_length=100)
    ndesc = models.TextField()
    npic = models.ImageField(upload_to='static/news/', defalt="")

    def __str__(self):
        return self.nhead