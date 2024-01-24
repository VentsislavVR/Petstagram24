from django.contrib import admin

from petstagram.common.models import Comment, Like


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'date_time_of_publication')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_photo')

