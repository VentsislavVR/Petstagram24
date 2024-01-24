from django.contrib import admin

from petstagram.photos import models


# Register your models here.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','date_of_publication',
                    'description','get_tagged_pets','get_likes_count', 'get_comments')

    @staticmethod
    def get_tagged_pets(obj):
        return ",".join([pet.name for pet in obj.tagged_pets.all()])
    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()
    @staticmethod
    def get_comments(obj):
        return ', '.join([str(comment.text) for comment in obj.comments.all()])