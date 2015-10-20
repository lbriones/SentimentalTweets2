from django.db import models

# Create your models here.

class UserTw(models.Model):

    screen_name = models.CharField(u'Screen name', max_length=50)
    screen_id 	= models.CharField(u'Id', max_length=100, blank=True, unique=True)
    description = models.TextField(u'Description', blank=True, null=True)
    timeline 	= models.TextField(u'Timeline', blank=True, null=True)

class Status(models.Model):

    usertw 	= models.TextField(u'UserTw', blank=True)
    text 	= models.TextField(u'Tweet', blank=True, null=True)
