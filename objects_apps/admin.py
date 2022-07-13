from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)