import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.models import Like
from petstagram.common.utils import get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo



def index(request):
    all_photos = Photo.objects.all()
    pet_name_pattern = request.GET.get('pet_name_pattern', None)

    if pet_name_pattern:
        all_photos = all_photos.filter(tagged_pets__name__icontains=pet_name_pattern)
        # Todo filter also by description and tagged

    context = {
        'all_photos': all_photos,
        'pet_name_pattern': pet_name_pattern

    }
    return render(
        request,
        'common/index.html',
        context
    )


def photo_share(request, photo_id):
    # Construct the absolute URL of the photo details page
    photo_details_url = request.build_absolute_uri(reverse('photo_details', kwargs={'pk': photo_id}))

    # Copy the URL to the clipboard
    pyperclip.copy(photo_details_url)

    # Redirect the user to another page (if needed)
    return redirect(get_photo_url(request, photo_id))


def photo_like(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_object = Like.objects.filter(to_photo=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        Like.objects.create(to_photo=photo)

    # Redirect the user to another page (if needed)

    return redirect(get_photo_url(request, photo_id))
