from django.contrib import admin
from .models import Post, Event, Slideshow

# Register your models here.
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Slideshow)