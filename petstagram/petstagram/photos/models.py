from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxFileSizeValidator, SIZE_5_MB, validate_file_size

UserModel = get_user_model()
# Create your models here.
class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(
            # MaxFileSizeValidator(limit_value=SIZE_5_MB),
            validate_file_size,
        ),
        blank=False,
        null=False,
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),

    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

