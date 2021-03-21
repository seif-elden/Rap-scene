from django.contrib import admin
from .models import Team_Member  , rapper , article , ad
# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models



admin.site.register(Team_Member)
admin.site.register(rapper)
admin.site.register(article)
admin.site.register(ad)
