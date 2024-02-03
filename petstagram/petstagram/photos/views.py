from django.shortcuts import render

from petstagram.photos.models import Photo


def photo_add(request):
    context = {}
    return render(
        request,
        'photos/photo-add-page.html',
        context
    )


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.likes.count()
    comments = photo.comments.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(
        request,
        'photos/photo-details-page.html',
        context
    )


def photo_edit(request, pk):
    context = {}
    return render(
        request,
        'photos/photo-edit-page.html',
        context
    )
