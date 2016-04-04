from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User)
    message_text = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)
    comment_text = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)



