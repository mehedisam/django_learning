from django.contrib import admin
from .models import WatchList, StreamList,Review
# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamList)
admin.site.register(Review)