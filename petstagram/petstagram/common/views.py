import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.models import Like
from petstagram.common.utils import get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo



def index(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }
    return render(
        request,
        'common/home-page.html',
        context
    )

# def index(request):
#     # search_form = SearchPhotosForm(request.GET)
#     search_pattern = None
#     # if search_form.is_valid():
#     #     search_pattern = search_form.cleaned_data['pet_name']
#
#     photos = Photo.objects.all()
#
#     if search_pattern:
#         photos = photos.filter(tagged_pets__name__icontains=search_pattern)
#
#     photos = [apply_likes_count(photo) for photo in photos]
#     photos = [apply_user_liked_photo(photo) for photo in photos]
#     print(photos)
#     context = {
#         'photos': photos,
#         # 'comment_form': PhotoCommentForm(),
#         # 'search_form': search_form,
#     }

    # return render(
    #     request,
    #     'common/home-page.html',
    #     context,
    # )


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
        like = Like(to_photo=photo)
        like.save()

    return redirect(get_photo_url(request, photo_id))
