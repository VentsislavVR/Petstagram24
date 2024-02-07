from django.db import models
from django.utils.text import slugify


# Create your models here.
class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )
    personal_photo = models.URLField(
        null=False,
        blank=False
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False, # Readonly,django_migrations
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.name}'

