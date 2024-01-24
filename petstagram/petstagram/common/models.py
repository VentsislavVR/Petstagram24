from django.db import models

from petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE, # TODO better to use do_nothing
        related_name='comments'

    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='likes'
    )
