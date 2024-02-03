from django.contrib import admin
from django.utils.html import format_html

from petstagram.photos import models


# Register your models here.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication',
                    'short_description', 'get_tagged_pets', 'get_likes_count', 'get_comments',)

    @staticmethod
    def get_tagged_pets(obj):
        return ",".join([pet.name for pet in obj.tagged_pets.all()])

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()

    @staticmethod
    def get_comments(obj):
        return ', '.join([str(comment.text) for comment in obj.comments.all()])
    @staticmethod
    def short_description(obj):
        return obj.description[:10]

    # def link_to_pet(self, obj):
    #     # Assuming obj has a field named 'pet_name' that you want to use in the URL
    #     return format_html('<a href="/path/to/pet/{0}/">{0}</a>',obj.tagged_pets)
    #
    # link_to_pet.allow_tags = True
    # link_to_pet.short_description = 'Pet Name'