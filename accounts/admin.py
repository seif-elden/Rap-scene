from django.contrib import admin
from .models import comments , community_post

# Register your models here.
def set_allVisable(modeladmin, request, queryset):
    for post in queryset:
        post.visable =  True
        post.save()
set_allVisable.short_description = 'aprove all posts'

class community_postAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'visable']
    list_filter  = ['visable',]
    fields = ["created_by","caption",'image_tag',"visable",]
    readonly_fields = ['image_tag']
    actions = [set_allVisable, ]


admin.site.register(comments)
admin.site.register(community_post,community_postAdmin)