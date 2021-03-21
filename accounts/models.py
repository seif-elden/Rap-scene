from django.db import models
from django.contrib.auth.models import User
from rapper.models import rapper

from django.utils.html import mark_safe

# Create your models here.

class community_post(models.Model):
    created_by = models.ForeignKey(User , related_name='community_post',on_delete=models.CASCADE)
    caption = models.TextField(max_length=150,blank=True)
    image = models.ImageField(blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    visable = models.BooleanField(default=False)
    
    class Meta:
        verbose_name : "music"
        verbose_name_plural : "musics"

    def __str__(self):
        return self.created_by.username


    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'



    

class comments(models.Model):
    community_post = models.ForeignKey(community_post,related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)