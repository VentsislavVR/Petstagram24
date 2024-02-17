import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.forms import CommentForm
from petstagram.common.models import Like
from petstagram.common.utils import get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo
from django.views import generic as views


# def index(request):
#     all_photos = Photo.objects.all()
#     pet_name_pattern = request.GET.get('pet_name_pattern', None)
#     comment_form = CommentForm()
#
#     if pet_name_pattern:
#         all_photos = all_photos.filter(tagged_pets__name__icontains=pet_name_pattern)
#         # Todo filter also by description and tagged
#
#     context = {
#         'all_photos': all_photos,
#         'pet_name_pattern': pet_name_pattern,
#         'comment_form': comment_form
#
#
#     }
#     return render(
#         request,
#         'common/index.html',
#         context
#     )
class IndexView(views.ListView):
    queryset = Photo.objects.all()\
        .prefetch_related('tagged_pets')\
        .prefetch_related('comments')\
        .prefetch_related('likes')\

    template_name = 'common/index.html'

    paginate_by = 1

    # def get_paginate_by(self, queryset):
    #     return self.request.GET.get('page_size', self.paginate_by)



    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', None)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pet_name_pattern'] = self.pet_name_pattern or ''

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_pet_name_pattern(queryset)
        return queryset.distinct('id')

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern
        filter_query = {}

        if pet_name_pattern:
            filter_query['tagged_pets__name__icontains'] = pet_name_pattern

        return queryset.filter(**filter_query)


def photo_share(request, photo_id):
    # Construct the absolute URL of the photo details page
    photo_details_url = request.build_absolute_uri(reverse('details photo', kwargs={'pk': photo_id}))

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


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()
            return request.META['HTTP_REFERER'] + f'#{photo_id}'
