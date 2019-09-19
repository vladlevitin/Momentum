from django.conf import settings
from django.db import models
from django.utils import timezone


# Post and users has a relationship since users can author a post. This is called a one-to-many relationship
# We solve this one-to-many relationship by using post-attribute of class "User" as foreignKey in weak-class Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    fp_image = models.ImageField(default='default.jpg', upload_to='news_pics', null=True)
    image = models.ImageField(default='default.jpg', upload_to='news_pics', null=True)
    preface = models.TextField(max_length=500, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # If a user is deleted, the post is also deleted

    def __str__(self):
        return self.title


# Events and users have a one-to-many relationship. Same structure as Post.
class Event(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='event_pics', help_text="Anbefalt størrelse: 800x200px", null=True)
    event_link = models.URLField(null=True)
    description = models.TextField(null=True)
    event_time = models.DateTimeField(auto_now=False)
    place = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # If a user is deleted, the event is also deleted

    def __str__(self):
        return self.title


class Slideshow(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='slideshow_pics', help_text="Påkrevd størrelse: 800x200px", null=True)
    slide_link = models.URLField(null=True)

    def __str__(self):
        return self.title
