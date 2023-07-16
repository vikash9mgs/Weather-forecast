from django.contrib import admin
from .models import *


# from .models import Subscribe
# Register your models here.


# admin.site.register(Subscribe)

class mnewsAdmin(admin.ModelAdmin):
    list_display = ('nhead', 'ntitle', 'ncity', 'ndesc', 'npic')


admin.site.register(mnews, mnewsAdmin)
